// ดึงข้อมูลชีตทั้งหมดที่อยู่ในฐานข้อมูล สร้าง dropdown list
function getProductionListsIPC(jwtToken) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    const ssMain = SpreadsheetApp.getActiveSpreadsheet();
    const shTabetLists = ssMain.getSheetByName(globalVariables().shTabetLists);
    const shProductionLists = ssMain.getSheetByName(globalVariables().shProductionLists);
    const tabetLists = shTabetLists.getDataRange().getDisplayValues().slice(1);
    const productionLists = shProductionLists.getDataRange().getDisplayValues().slice(1);

    let sheetListsIPC = [];

    if (verifyToken.userData.role != "Operator") {
      productionLists.forEach(([filename, type, sheetUrl, slidUrl])=> {
        if(type === "IPC") {
          sheetListsIPC.push({
            name: filename.toUpperCase(),
            url: sheetUrl,
            pdf: slidUrl.replace("edit?usp=drivesdk", "preview"),
          });
        }
      });

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

    tabetLists.reverse().forEach((data) => {
      const tablet_name = data[0].toUpperCase();
      const tablet_url_ipc = data[4];
      sheetListsIPC.push({
        name: `เครื่องตอก ${tablet_name} (LOT. ปัจจุบัน)`,
        url: tablet_url_ipc,
        pdf: null,
      });
    });

    return { result: verifyToken, productionLists: sheetListsIPC };
  }
}

// ดึงข้อมูลจากชีต จากหมายเลขเครื่องตอก URL
function getWeighingDataIPC({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
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
        recorder: row[4],
        role: row[5],
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
function signInToCheckTheSettingsIPC({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    const spreadsheet = SpreadsheetApp.openByUrl(url);
    const sheet = spreadsheet.getSheetByName(globalVariables().shSetWeight); // เข้าถึง sheet ตั้งค่าน้ำหนักยา
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
      timeZone: "Asia/Bangkok",
    });
    const approval_msg = `🌈ระบบเครื่องชั่ง IPC\
                        \n🔰ชื่อยา ${settingDetail.productName}\
                        \n🔰เลขที่ผลิต ${settingDetail.lot}\
                        \n🔰เครื่องตอก ${settingDetail.tabletID}\n
                        \n⪼ ตรวจสอบการตั้งค่าโดย\
                        \n⪼ คุณ ${verifyToken.userData.nameTH}\
                        \n⪼ ${timestamp}`;

    sendLineNotify(approval_msg, globalVariables().approvalToken);
    return { result: verifyToken };
  }
}

// สิ้นสุดการผลิต
function endOfProductionIPC({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    const today = new Date().toLocaleString("en-GB", {
      timeZone: "Asia/Bangkok",
    });
    const date = new Date().toLocaleDateString("en-GB", {
      timeZone: "Asia/Bangkok",
    });

    const spreadsheet = SpreadsheetApp.openByUrl(url);
    const shSetWeight = spreadsheet.getSheetByName(
      globalVariables().shSetWeight
    );

    // บันทึกชื่อ,วันที่ เวลา จบการผลิต
    shSetWeight
      .getRange(globalVariables().finishedIPC)
      .setValue(verifyToken.userData.nameTH);
    shSetWeight.getRange(globalVariables().finishTimeIPC).setValue(today);

    // บันทึกการปฏิบัติงาน
    const productName = shSetWeight
      .getRange(globalVariables().finishRangesIPC.productname)
      .getDisplayValue();
    const lot = shSetWeight
      .getRange(globalVariables().finishRangesIPC.lot)
      .getDisplayValue();
    const tabletID = shSetWeight
      .getRange(globalVariables().finishRangesIPC.tabletID)
      .getDisplayValue();

    const details = `ระบบเครื่องชั่ง: IPC\
                \nชื่อยา: ${productName}\
                \nเลขที่ผลิต: ${lot}\
                \nเครื่องตอก: ${tabletID}`;

    recordAuditTrailData({
      list: "จบการผลิต",
      details: details,
      username: verifyToken.userData.nameTH,
      role: verifyToken.userData.role,
    });

    // จัดเก็บข้อมูลไปยังโฟล์เดอร์
    const folder = DriveApp.getFolderById(globalVariables().folderIdIPC);
    const newSh = spreadsheet.copy(`${lot}_${productName}_${tabletID}_${date}`);
    const shUrl = newSh.getUrl(); // get newSheetID
    const shID = newSh.getId(); // get newSheetID
    const file = DriveApp.getFileById(shID);

    folder.addFile(file); // ย้ายไฟล์ไปยังแฟ้มเก็บข้อมูล

    // เคลียร์ข้อมูลชีตต้นฉบับ
    spreadsheet
      .getSheetByName(globalVariables().shWeightIPC)
      .getRange(globalVariables().finishRangesIPC.clearRanges.weighing)
      .clearContent();
    spreadsheet
      .getSheetByName(globalVariables().shRemarks)
      .getRange(globalVariables().finishRangesIPC.clearRanges.remarks)
      .clearContent();
    spreadsheet
      .getSheetByName(globalVariables().shSetWeight)
      .getRange(globalVariables().setupRangeIPC)
      .setValue(globalVariables().finishRangesIPC.clearRanges.settingText);

    return { result: verifyToken, urlCreatePDF: shUrl };
  }
}


// สร้างไฟล์ slide,pdf
function createPdfIPC({ url, jwtToken }) {
  const getData = getWeighingDataIPC({ url: url, jwtToken: jwtToken });
  if (getData.result.message != "success") {
    return { result: getData.result };
  }
  else {
    const settingDetail = getData.dataset.settingDetail;
    const weighingData = getData.dataset.weighingData.reverse();
    const remarksData = getData.dataset.remarksData.reverse();

    const slideFolder = DriveApp.getFolderById(globalVariables().slideFolderIdIPC); // folder Slide
    const slideTemplate = DriveApp.getFileById(globalVariables().slideTemplateIdIPC); // Templete SlideID
    const newSlideCopy = slideTemplate.makeCopy(slideFolder);
    const today = new Date().toLocaleDateString("en-GB", {
      timeZone: "Asia/Bangkok",
    });
    newSlideCopy.setName(
      [settingDetail.lot, settingDetail.productName, today].join("_")
    );

    const newSlide = SlidesApp.openById(newSlideCopy.getId());

    const slides = newSlide.getSlides();
    const detailSlide = slides[0];
    const remarksSlide = slides[1];
    const weighingSlide = slides[2];

    newSlide.replaceAllText("{productname}", settingDetail.productName);
    newSlide.replaceAllText("{lot}", settingDetail.lot);
    newSlide.replaceAllText("{balanceID}", settingDetail.balanceID);
    newSlide.replaceAllText("{tabletID}", settingDetail.tabletID);
    newSlide.replaceAllText("{punches}", settingDetail.numberPunches);
    newSlide.replaceAllText("{numtablets}", settingDetail.numberTablets);
    newSlide.replaceAllText("{meanWeight}", settingDetail.meanWeight);
    newSlide.replaceAllText("{percent}", settingDetail.percentWeightVariation);
    newSlide.replaceAllText("{AVGmin}", settingDetail.meanWeightAvgMin);
    newSlide.replaceAllText("{AVGmax}", settingDetail.meanWeightAvgMax);
    newSlide.replaceAllText("{IHmin}", settingDetail.meanWeightInhouseMin);
    newSlide.replaceAllText("{IHmax}", settingDetail.meanWeightInhouseMax);
    newSlide.replaceAllText("{REGmin}", settingDetail.meanWeightRegMin);
    newSlide.replaceAllText("{REGmax}", settingDetail.meanWeightRegMax);
    newSlide.replaceAllText("{prepared}", settingDetail.prepared);
    newSlide.replaceAllText("{approved}", settingDetail.approved);
    newSlide.replaceAllText("{finished}", settingDetail.finished);
    newSlide.replaceAllText("{finishTime}", settingDetail.finishTime);

    const remarksTable = remarksSlide.getTables()[0];
    remarksData.forEach((dataRow, index) => {
      if (index > 0 && remarksTable.getNumRows() - 1 < remarksData.length) {
        remarksTable.appendRow();
      }

      const row = index + 1;
      remarksTable.getRow(row).getCell(0).getText().setText(dataRow.timestamp);
      remarksTable.getRow(row).getCell(1).getText().setText(dataRow.issues);
      remarksTable.getRow(row).getCell(2).getText().setText(dataRow.cause);
      remarksTable.getRow(row).getCell(3).getText().setText(dataRow.resolve);
      remarksTable.getRow(row).getCell(4).getText().setText(dataRow.recorder);
      remarksTable.getRow(row).getCell(5).getText().setText(dataRow.role);
    });

    const numTable = 4;
    const totalPages = Math.ceil(weighingData.length / numTable);
    let totalWeight = [];
    let sumTotalWeight = 0;

    for (let i = 0; i < totalPages; i++) {
      let slide;
      if (i == totalPages - 1) {
        slide = weighingSlide;
      } else {
        slide = weighingSlide.duplicate();
      }

      slide.move(newSlide.getSlides().length);
      for (let ix = 0; ix < numTable; ix++) {
        const dataLength = (numTable * i) + ix;
        if (dataLength < weighingData.length) {
          const dataset = weighingData[dataLength];
          let _timestamp = [];
          let _weights = [];
          let sumWeight = 0;
          dataset.weights.forEach((data) => {
            _timestamp.push(data.timestamp);
            _weights.push(data.weight);
            sumWeight += parseFloat(data.weight);

            if (
              parseFloat(data.weight) >=
              parseFloat(settingDetail.meanWeightRegMin) &&
              parseFloat(data.weight) <=
              parseFloat(settingDetail.meanWeightRegMax)
            ) {
              sumTotalWeight += parseFloat(data.weight);
              totalWeight.push(parseFloat(data.weight));
            }
          });

          const timestamp = _timestamp.join("\n");
          const weights = _weights.join("\n");
          const min = Math.min(..._weights).toFixed(3);
          const max = Math.max(..._weights).toFixed(3);
          const average = (sumWeight / dataset.weights.length).toFixed(3);

          const table = slide.getTables()[ix];
          const datetimeCell = table.getRow(0).getCell(0);
          const timestampCell = table.getRow(2).getCell(0);
          const weightCell = table.getRow(2).getCell(1);
          const averageCell = table.getRow(3).getCell(1);
          const minCell = table.getRow(5).getCell(0);
          const maxCell = table.getRow(5).getCell(1);
          const characteristicsCell = table.getRow(6).getCell(1);
          const operatorCell = table.getRow(7).getCell(1);

          datetimeCell.getText().setText(dataset.datetime);
          timestampCell.getText().setText(timestamp);
          weightCell.getText().setText(weights);
          averageCell.getText().setText(average);
          minCell.getText().setText(min);
          maxCell.getText().setText(max);
          characteristicsCell.getText().setText(dataset.characteristics);
          operatorCell.getText().setText(dataset.operator);

          if (dataLength == 0) {
            detailSlide.replaceAllText("{startTime}", dataset.datetime);
          }
        }
        else {
          break;
        }
      }
    }

    detailSlide.replaceAllText("{summin}", Math.min(...totalWeight).toFixed(3));
    detailSlide.replaceAllText("{summax}", Math.max(...totalWeight).toFixed(3));
    detailSlide.replaceAllText(
      "{sumavg}",
      (sumTotalWeight / totalWeight.length).toFixed(3)
    );

    const mainSpreadSheet = SpreadsheetApp.getActiveSpreadsheet();
    const mainProductionLists = mainSpreadSheet.getSheetByName(
      globalVariables().shProductionLists
    );
    mainProductionLists.appendRow([
      SpreadsheetApp.openByUrl(url).getName(),
      "IPC",
      url,
      newSlideCopy.getUrl(),
    ]);

    return { result: getData.result };
  }
}
