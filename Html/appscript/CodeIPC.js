// ดึงข้อมูลชีตทั้งหมดที่อยู่ในฐานข้อมูล สร้าง dropdown list
function getProductionListsIpc() {
  const verifyToken = validateToken();

  if (verifyToken.message != "success") {
    return;
  }
  else {
    let folderIdIPC = globalVariables().folderIdIPC;
    let folderIPC = DriveApp.getFolderById(folderIdIPC);
    let contentsIPC = folderIPC.getFiles();

    let sheetListsIPC = [];

    const fileType = "application/vnd.google-apps.spreadsheet";
    if (verifyToken.data.role != "Operator") {
      while (contentsIPC.hasNext()) {
        let file = contentsIPC.next();
        if (file.getMimeType() === fileType) {
          const tablet_name = file.getName().toUpperCase();
          const tablet_url_10s = file.getUrl();
          sheetListsIPC[tablet_name] = tablet_url_10s;
        };
      };
    };

    // // จัดเรียงข้อมูลตามวันที่
    // listsIPC = sheetListsIPC.sort((item1, item2) => {
    //   const date1Parts = item1[0].split('_').pop().split('/');
    //   const date2Parts = item2[0].split('_').pop().split('/');
    //   const date1 = new Date(`${date1Parts[2]}-${date1Parts[1]}-${date1Parts[0]}`);
    //   const date2 = new Date(`${date2Parts[2]}-${date2Parts[1]}-${date2Parts[0]}`);
    //   return date1 - date2;
    // });

    let ssMain = SpreadsheetApp.getActiveSpreadsheet();
    let shTabetList = ssMain.getSheetByName(globalVariables().shTabetList);

    let lists = shTabetList.getDataRange().getDisplayValues().slice(1);
    lists.reverse().forEach(data => {
      const tablet_name = data[0].toUpperCase();
      const tablet_url_ipc = data[5];
      sheetListsIPC.push({
        name: `เครื่องตอก ${tablet_name} (LOT. ปัจจุบัน)`,
        url: tablet_url_ipc,
      });
    });

    console.log(sheetListsIPC);
    return sheetListsIPC;
  }
}

// ดึงข้อมูลจากชีต จากหมายเลขเครื่องตอก URL
function getCurrentData_IPC(url) {
  let ssIPC = SpreadsheetApp.openByUrl(url);
  let sheetRemarksIPC = ssIPC.getSheetByName(globalVariables().shRemarks);
  let ranges = globalVariables().dataRangeIPC.reverse();
  let summaryRanges = globalVariables().summaryRangeIPC.reverse();

  let result = [];

  // ดึงข้อมูลน้ำหนักยา
  let shIPC = ssIPC.getSheets();
  let shName
  let sheetIPC,
    data,
    colors,
    dataSummary,
    colorsSummary

  shIPC.forEach(sh => {
    shName = sh.getSheetName();
    if (!["Remark", "USER", "Setting"].includes(shName)) {
      ranges.forEach((range, index) => {
        sheetIPC = ssIPC.getSheetByName(shName);
        data = sheetIPC.getRange(range).getDisplayValues();
        colors = sheetIPC.getRange(range).getBackgrounds();

        dataSummary = sheetIPC.getRange(summaryRanges[index]).getDisplayValues();
        colorsSummary = sheetIPC.getRange(summaryRanges[index]).getBackgrounds();

        result.push({
          shName: shName,
          data: data,
          colors: colors,
          dataSummary: dataSummary,
          colorsSummary: colorsSummary
        });

      });
    };
  });

  let sheetSetupIPC = ssIPC.getSheetByName(globalVariables().shSetWeight);
  let setupWeightIPC = sheetSetupIPC.getRange(globalVariables().setupRangeIPC).getDisplayValues();
  let remarks = sheetRemarksIPC.getDataRange().getDisplayValues().slice(2).reverse();

  return { result, setupWeightIPC, remarks, url };
}

// ลงชื่อผู้ตรวจสอบการตั้งค่า
function setting_addChecker_ipc(url, username, detail) {
  let spreadsheet = SpreadsheetApp.openByUrl(url);
  let sheet = spreadsheet.getSheetByName(globalVariables().shSetWeight);

  sheet.getRange(globalVariables().checkSetupRangeIPC).setValue(username);

  // บันทึกการปฏิบัติงาน
  let auditTrial_msg = `ระบบเครื่องชั่ง ${detail.type}\
                      \n${detail.product}\
                      \n${detail.lot}\
                      \n${detail.tabletID}`;

  audit_trail("ลงชื่อตรวจสอบการตั้งค่า", auditTrial_msg, username);

  const timeStamp = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Jakarta' });
  const approval_msg = `🌈ระบบเครื่องชั่ง ${detail.type}
    \n🔰${detail.tabletID}\
    \n🔰${detail.lot}\
    \n🔰${detail.product}
    \n⪼ ตรวจสอบการตั้งค่าโดย\
    \n⪼ คุณ ${username}\
    \n⪼ ${timeStamp}`;

  sendLineNotify(approval_msg, globalVariables().approval_token);
}

// บันทึกสรุปข้อมูลการชั่งน้ำหนัก
function summaryRecord_IPC(url, min, max, average) {
  let spreadsheet = SpreadsheetApp.openByUrl(url);
  let sheet = spreadsheet.getSheetByName(globalVariables().shSetWeight);
  let ranges = sheet.getRange(globalVariables().summaryRecordRangeIPC);
  ranges.setValues([[min], [max], [average]]);
  ranges.setNumberFormats([['0.000'], ['0.000'], ['0.000']]);
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
    };
  });
}

// สิ้นสุดการผลิต
function endJob_IPC(url, username) {
  let spreadsheet = SpreadsheetApp.openByUrl(url);
  let today = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Jakarta' });
  let date = today.split(",")[0];

  let shSetWeight = spreadsheet.getSheetByName(globalVariables().shSetWeight);
  let tabletID = shSetWeight.getRange('A4').getDisplayValue();
  let productName = shSetWeight.getRange('A6').getDisplayValue();
  let lot = shSetWeight.getRange('A8').getDisplayValue();

  // บันทึกคนที่กด ENDJOB
  shSetWeight.getRange(globalVariables().checkEndjobRangeIPC).setValue("จบการผลิตโดย " + username + " วันที่ " + today);

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
  };

  spreadsheet.getSheetByName(globalVariables().shWeightIPC).getRangeList(["A17:K17", "A19:K68"]).clearContent();
  spreadsheet.getSheetByName(globalVariables().shWeightIPC).getRangeList(["B73:B78", "E73:E78", "H73:H78", "K73:K78"]).clearContent();
  spreadsheet.getSheetByName(globalVariables().shRemarks).getRange("A3:F").clearContent();
  spreadsheet.getSheetByName(globalVariables().shSetWeight).getRange("A3").setValue("A19:B68");
  spreadsheet.getSheetByName(globalVariables().shSetWeight).getRange("A5:A20").setValue("xxxxx");
  spreadsheet.getSheetByName(globalVariables().shSetWeight).getRange("G2:G4").setValue("xxxxx");

  return getCurrentData_IPC(url);
};
