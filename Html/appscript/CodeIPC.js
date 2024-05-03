// ดึงข้อมูลชีตทั้งหมดที่อยู่ในฐานข้อมูล สร้าง dropdown list
function getProductionListsIpc(jwtToken) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    let folderIdIPC = globalVariables().folderIdIPC;
    let folderIPC = DriveApp.getFolderById(folderIdIPC);
    let contentsIPC = folderIPC.getFiles();

    let sheetListsIPC = [];

    const fileType = "application/vnd.google-apps.spreadsheet";
    if (verifyToken.userData.role != "Operator") {
      while (contentsIPC.hasNext()) {
        let file = contentsIPC.next();
        if (file.getMimeType() === fileType) {
          const tablet_name = file.getName().toUpperCase();
          const tablet_url_ipc = file.getUrl();
          sheetListsIPC.push({
            name: tablet_name,
            url: tablet_url_ipc,
          });
        }
      }
    }

    // จัดเรียงข้อมูลตามวันที่
    sheetListsIPC = sheetListsIPC.sort((item1, item2) => {
      const date1Parts = item1.name.split("_").pop().split("/");
      const date2Parts = item2.name.split("_").pop().split("/");
      const date1 = new Date(
        `${date1Parts[2]}-${date1Parts[1]}-${date1Parts[0]}`
      );
      const date2 = new Date(
        `${date2Parts[2]}-${date2Parts[1]}-${date2Parts[0]}`
      );
      return date1 - date2;
    });

    let ssMain = SpreadsheetApp.getActiveSpreadsheet();
    let shTabetList = ssMain.getSheetByName(globalVariables().shTabetList);

    let lists = shTabetList.getDataRange().getDisplayValues().slice(1);
    lists.reverse().forEach((data) => {
      const tablet_name = data[0].toUpperCase();
      const tablet_url_ipc = data[5];
      sheetListsIPC.push({
        name: `เครื่องตอก ${tablet_name} (LOT. ปัจจุบัน)`,
        url: tablet_url_ipc,
      });
    });

    return { result: verifyToken, productionLists: sheetListsIPC };
  }
}

// ดึงข้อมูลจากชีต จากหมายเลขเครื่องตอก URL
function getWeighingData_IPC(jwtToken, url) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return verifyToken.message;
  } else {
    // const url = "https://docs.google.com/spreadsheets/d/1Z_yI1KQp2YCoDHp8T3Zs5Pw1JMVt3thdrxUnArUv-bo/edit#gid=596757621";
    const spreadsheet = SpreadsheetApp.openByUrl(url); // เข้าถึง Spreadsheet
    const data_setting = spreadsheet
      .getSheetByName(globalVariables().shSetWeight) // เข้าถึง sheet ตั้งค่าน้ำหนักยา
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    const data_weighing = spreadsheet
      .getSheetByName(globalVariables().shWeightIPC) // เข้าถึง sheet ชั่งน้ำหนัก
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    const data_remarks = spreadsheet
      .getSheetByName(globalVariables().shRemarks) // เข้าถึง sheet remarks
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    // สร้างข้อมูลการตั้งค่าน้ำหนักยา
    const settingDetail = {
      productName: data_setting[0][1], // ชื่อยา
      lot: data_setting[1][1], // เลขที่ผลิต
      balanceID: data_setting[2][1], // เครื่องชั่ง
      tabletID: data_setting[3][1], // เครื่องตอก
      numberPunches: data_setting[4][1], // จำนวนสาก
      numberTablets: data_setting[5][1], // จำนวนเม็ดที่ต้องชั่ง
      meanWeight: data_setting[6][1], // น้ำหนักตามทฤษฎี
      percentWeightVariation: data_setting[7][1], // เปอร์เซ็นเบี่ยงเบน
      meanWeightAvgMin: data_setting[8][1], // ช่วงน้ำหนักเฉลี่ยที่ยอมรับ(Min.)
      meanWeightAvgMax: data_setting[9][1], // ช่วงน้ำหนักเฉลี่ยที่ยอมรับ(Max.)
      meanWeightInhouseMin: data_setting[10][1], // ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ (Min.)
      meanWeightInhouseMax: data_setting[11][1], // ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ (Max.)
      meanWeightRegMin: data_setting[12][1], // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
      meanWeightRegMax: data_setting[13][1], // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
      prepared: data_setting[14][1], // ตั้งค่าน้ำหนักโดย
      approved: data_setting[15][1], // ตรวจสอบการตั้งค่าโดย
      finished: data_setting[16][1], // จบการผลิตโดย
      finishTime: data_setting[17][1], // จบการผลิตเวลา
    };

    let weighingData = []; // สร้างตัวแปรไว้เก็บข้อมูลแบบ object
    data_weighing.forEach((item, index) => {
      if (index % 2 === 0) {
        let rowData = {
          datetime: item[0], // เก็บข้อมูลเวลา
          operator: item[1], // เก็บข้อมูลผู้ปฎิบัติงาน
          type: item[2], // เก็บประเภทข้อมูล
          characteristics: item[3], // เก็บข้อมูลลักษณะเม็ดยา
          weights: [],
        };

        const slice_num = 5; // จำนวน index ที่ตัดออก
        const weightValues = item.slice(slice_num); // ตัดข้อมูลออก 5 คลอลั่ม

        weightValues.forEach((timestamp, idx) => {
          const weight = data_weighing[index + 1][idx + slice_num];
          if (timestamp) {
            rowData["weights"].push({
              timestamp: timestamp,
              weight: weight,
            });
          }
        });

        console.log(rowData);
        weighingData.push(rowData);
      }
    });

    // สร้างข้อมูลการ remarks
    let remarksData = [];
    data_remarks.forEach((row) => {
      const rowData = {
        timestamp: row[0],
        issues: row[1],
        cause: row[2],
        resolve: row[3],
        notes: row[4],
        recorder: row[5],
        role: row[6],
      };

      // นำข้อมูลการชั่งแต่ล่ะครั้งไปเก็บใน dataObj
      remarksData.push(rowData);
    });

    const dataset = {
      settingDetail: settingDetail,
      weighingData: weighingData.reverse(),
      remarksData: remarksData.reverse(),
    };

    return { result: verifyToken, dataset: dataset };
  }
}

// ลงชื่อผู้ตรวจสอบการตั้งค่า
// ลงชื่อผู้ตรวจสอบการตั้งค่า
function signInToCheckTheSettingsIPC({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return verifyToken.message;
  } else {
    const spreadsheet = SpreadsheetApp.openByUrl(url);
    const sheet = spreadsheet.getSheetByName(globalVariables().shSetWeight);  // เข้าถึง sheet ตั้งค่าน้ำหนักยา
    const data_setting = sheet 
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    // ลงชื่อผู้ตรวจสอบการตั้งค่า
    sheet
      .getRange(globalVariables().approvedRangeIPC)
      .setValue(verifyToken.userData.nameTH);

    // สร้างข้อมูลการตั้งค่าน้ำหนักยา
    const settingDetail = {
      productName: data_setting[0][1], // ชื่อยา
      lot: data_setting[1][1], // เลขที่ผลิต
      tabletID: data_setting[3][1], // เครื่องตอก
    };

    // บันทึกการปฏิบัติงาน
    const details = `ระบบเครื่องชั่ง IPC\
                    \nชื่อยา ${settingDetail.productName}\
                    \nเลขที่ผลิต ${settingDetail.lot}\
                    \nเครื่องตอก ${settingDetail.tabletID}`;

    recordAuditTrailData({
      list: "ลงชื่อตรวจสอบการตั้งค่า",
      details: details,
      username: verifyToken.userData.nameTH,
      role: verifyToken.userData.role,
    });

    const timestamp = new Date().toLocaleString("en-GB", {
      timeZone: "Asia/Jakarta",
    });
    const approval_msg = `🌈ระบบเครื่องชั่ง IPC\
                        \nชื่อยา ${settingDetail.productName}\
                        \nเลขที่ผลิต ${settingDetail.lot}\
                        \nเครื่องตอก ${settingDetail.tabletID}\
                        \n⪼ ตรวจสอบการตั้งค่าโดย\
                        \n⪼ คุณ ${verifyToken.userData.nameTH}\
                        \n⪼ ${timestamp}`;

    sendLineNotify(approval_msg, globalVariables().approval_token);
    return { result: verifyToken };
  }
}

// บันทึกสรุปข้อมูลการชั่งน้ำหนัก
function summaryRecord_IPC(url, min, max, average) {
  let spreadsheet = SpreadsheetApp.openByUrl(url);
  let sheet = spreadsheet.getSheetByName(globalVariables().shSetWeight);
  let ranges = sheet.getRange(globalVariables().summaryRecordRangeIPC);
  ranges.setValues([[min], [max], [average]]);
  ranges.setNumberFormats([["0.000"], ["0.000"], ["0.000"]]);
}

// บันทึกลัษณะของเม็ดยา
function setTabletDetail_IPC(url, sheetName, date_time, text) {
  let spreadsheet = SpreadsheetApp.openByUrl(url);
  let sheet = spreadsheet.getSheetByName(sheetName);

  let ranges_getTimestamp = globalVariables().timestampRangeIPC;
  let ranges_setText = globalVariables().tabletDetailRangeIPC;

  ranges_getTimestamp.forEach((range, i) => {
    let timeStamp = sheet.getRange(range).getDisplayValue();
    if (timeStamp == date_time) {
      sheet.getRange(ranges_setText[i]).setValue(text);
    }
  });
}

// สิ้นสุดการผลิต
function endJob_IPC(url, username) {
  let spreadsheet = SpreadsheetApp.openByUrl(url);
  let today = new Date().toLocaleString("en-GB", { timeZone: "Asia/Jakarta" });
  let date = today.split(",")[0];

  let shSetWeight = spreadsheet.getSheetByName(globalVariables().shSetWeight);
  let tabletID = shSetWeight.getRange("A4").getDisplayValue();
  let productName = shSetWeight.getRange("A6").getDisplayValue();
  let lot = shSetWeight.getRange("A8").getDisplayValue();

  // บันทึกคนที่กด ENDJOB
  shSetWeight
    .getRange(globalVariables().checkEndjobRangeIPC)
    .setValue("จบการผลิตโดย " + username + " วันที่ " + today);

  // บันทึกการปฏิบัติงาน
  let detail = `ระบบเครื่องชั่ง: IPC\
                \nชื่อยา: ${productName}\
                \nเลขที่ผลิต: ${lot}\
                \nเครื่องตอก: ${tabletID}`;

  audit_trail("จบการผลิต", detail, username);

  // จัดเก็บข้อมูลไปยังโฟล์เดอร์
  let folder = DriveApp.getFolderById(globalVariables().folderIdIPC);
  let newSh = spreadsheet.copy(`${lot}_${productName}_${tabletID}_IPC_${date}`);
  let shID = newSh.getId(); // get newSheetID
  let file = DriveApp.getFileById(shID);

  folder.addFile(file); // ย้ายไฟล์ไปยังแฟ้มเก็บข้อมูล

  // ลบชีตที่ไม่ใช่ชีตหลักออก
  let shName = spreadsheet.getSheets();
  for (i = 0; i < shName.length; i++) {
    let sh = shName[i].getName();
    if (sh == "Weight Variation" || sh == "Remark" || sh == "Setting") {
      continue;
    } else {
      spreadsheet.deleteSheet(shName[i]);
    }
  }

  spreadsheet
    .getSheetByName(globalVariables().shWeightIPC)
    .getRangeList(["A17:K17", "A19:K68"])
    .clearContent();
  spreadsheet
    .getSheetByName(globalVariables().shWeightIPC)
    .getRangeList(["B73:B78", "E73:E78", "H73:H78", "K73:K78"])
    .clearContent();
  spreadsheet
    .getSheetByName(globalVariables().shRemarks)
    .getRange("A3:F")
    .clearContent();
  spreadsheet
    .getSheetByName(globalVariables().shSetWeight)
    .getRange("A3")
    .setValue("A19:B68");
  spreadsheet
    .getSheetByName(globalVariables().shSetWeight)
    .getRange("A5:A20")
    .setValue("xxxxx");
  spreadsheet
    .getSheetByName(globalVariables().shSetWeight)
    .getRange("G2:G4")
    .setValue("xxxxx");

  return getCurrentData_IPC(url);
}
