// ดึงข้อมูลชีตทั้งหมดที่อยู่ในฐานข้อมูล สร้าง dropdown list
function getProductionList(jsonWebToken, nameTH) {
  const verify_token = validateToken(jsonWebToken, nameTH);

  if (verify_token.message != "success") {
    return verify_token;
  }
  else {
    let folderId10s = globalVariables().folderId10s;
    let folder10s = DriveApp.getFolderById(folderId10s);
    let contents10s = folder10s.getFiles();

    let folderIdIPC = globalVariables().folderIdIPC;
    let folderIPC = DriveApp.getFolderById(folderIdIPC);
    let contentsIPC = folderIPC.getFiles();

    let sheetLists10s = [];
    let sheetListsIPC = [];

    const fileType = "application/vnd.google-apps.spreadsheet";
    if (verify_token.token.data.role != "Operator") {
      while (contentsIPC.hasNext()) {
        let file = contentsIPC.next();
        if (file.getMimeType() === fileType) {
          const tablet_name = file.getName().toUpperCase();
          const tablet_url_10s = file.getUrl();
          sheetListsIPC.push([tablet_name, tablet_url_10s]);
        };
      };

      while (contents10s.hasNext()) {
        let file = contents10s.next();
        if (file.getMimeType() === fileType) {
          const tablet_name = file.getName().toUpperCase();
          const tablet_url_ipc = file.getUrl();
          sheetLists10s.push([tablet_name, tablet_url_ipc]);
        };
      };
    };

    // จัดเรียงข้อมูลตามวันที่
    sheetLists10s = sheetLists10s.sort((item1, item2) => {
      const date1Parts = item1[0].split('_').pop().split('/');
      const date2Parts = item2[0].split('_').pop().split('/');
      const date1 = new Date(`${date1Parts[2]}-${date1Parts[1]}-${date1Parts[0]}`);
      const date2 = new Date(`${date2Parts[2]}-${date2Parts[1]}-${date2Parts[0]}`);
      return date1 - date2;
    });

    // จัดเรียงข้อมูลตามวันที่
    sheetListsIPC = sheetListsIPC.sort((item1, item2) => {
      const date1Parts = item1[0].split('_').pop().split('/');
      const date2Parts = item2[0].split('_').pop().split('/');
      const date1 = new Date(`${date1Parts[2]}-${date1Parts[1]}-${date1Parts[0]}`);
      const date2 = new Date(`${date2Parts[2]}-${date2Parts[1]}-${date2Parts[0]}`);
      return date1 - date2;
    });

    let ssMain = SpreadsheetApp.getActiveSpreadsheet();
    let shTabetList = ssMain.getSheetByName(globalVariables().shTabetList);

    let dataLists = shTabetList.getDataRange().getDisplayValues().slice(1);
    dataLists.reverse().forEach(data => {
      const tablet_name = data[0].toUpperCase();
      const tablet_url_10s = data[3];
      const tablet_url_ipc = data[5];
      sheetLists10s.push([`เครื่องตอก ${tablet_name} (LOT. ปัจจุบัน)`, tablet_url_10s]);
      sheetListsIPC.push([`เครื่องตอก ${tablet_name} (LOT. ปัจจุบัน)`, tablet_url_ipc])
    });

    return { message: "success", sheetLists10s, sheetListsIPC };
  }
}

// ดึงข้อมูล Main_Setup สำหรับการตั้งค่าทั้งหมด
function getDataSetting() {
  const verify_token = validateToken();

  if (verify_token.message !== "success") {
    return;
  }
  else {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheetUsers = spreadsheet.getSheetByName(globalVariables().shUserList);
    const sheetTablet = spreadsheet.getSheetByName(globalVariables().shTabetList);
    const sheetScale = spreadsheet.getSheetByName(globalVariables().shScaleList);
    const sheetProductName = spreadsheet.getSheetByName(globalVariables().shProductNameList);

    const userDataLists = sheetUsers.getDataRange().getDisplayValues().slice(2);
    const tabletDataLists = sheetTablet.getDataRange().getDisplayValues().slice(1);
    const balanceDataLists = sheetScale.getDataRange().getDisplayValues().slice(1);
    const productNameDataLists = sheetProductName.getDataRange().getDisplayValues().slice(2);

    /** สร้างข้อมูลรายชื่อผู้ใช้งาน **/
    let userLists = {}; // สร้าง data object เก็บข้อมูล
    userDataLists.forEach((row) => {
      const rfid = row[0];
      const userList = {
        employeeId: row[1],
        usernameTH: row[2],
        usernameEN: row[3],
        role: row[5],
      };

      // เพิ่มข้อมูล user_data_list ไปยัง userList
      userLists[rfid] = userList;
    });

    /** สร้างข้อมูลรายชื่อเครื่องตอก **/
    let tabletLists = {}; // สร้าง data object เก็บข้อมูล
    tabletDataLists.forEach((row) => {
      const tabletID = row[0];
      const tabletList = {
        "url_10s": row[3],
        "url_ipc": row[5],
      };

      // เพิ่มข้อมูล user_data_list ไปยัง userList
      tabletLists[tabletID] = tabletList;
    });

    /** สร้างข้อมูลรายชื่อเครื่องชั่ง **/
    let balanceLists = []; // สร้าง data object เก็บข้อมูล
    balanceDataLists.forEach((row) => {
      const balanceID = row[0];
      balanceLists.push(balanceID); // เพิ่มข้อมูล user_data_list ไปยัง userList
    });

    /** สร้างข้อมูลรายชื่อยา **/
    let productLists = {}; // สร้าง data object เก็บข้อมูล
    productNameDataLists.forEach((row) => {
      const dataList = {}
      const productName = row[0].toUpperCase();
      // ตั้งค่าข้อมูลน้ำหนักยาแบบชั่ง 10 เม็ด
      const weight_control_10s = {
        meanWeight10s: row[1],
        percentWeightVariation10s: row[2],
        meanWeight10sMin: row[3],
        meanWeight10sMax: row[4],
        meanWeightReg10sMin: row[5],
        meanWeightReg10sMax: row[6],
        thickness10sMin: row[7],
        thickness10sMax: row[8]
      };

      const weight_control_ipc = {
        meanWeightIpc: row[9],
        percentWeightIpc: row[10],
        meanWeightAverageIpcMin: row[11],
        meanWeightAverageIpcMax: row[12],
        meanWeightVariationIpcMin: row[13],
        meanWeightVariationIpcMax: row[14],
        meanWeightRegIpcMin: row[15],
        meanWeightRegIpcMax: row[16]
      };

      // เพิ่มข้อมูล user_data_list ไปยัง userList
      dataList["weight_control_10s"] = weight_control_10s;
      dataList["weight_control_ipc"] = weight_control_ipc;

      productLists[productName] = dataList;
    });

    const data = {
      "userLists": userLists,
      "tabletLists": tabletLists,
      "balanceLists": balanceLists,
      "productLists": productLists
    };

    console.log(data.userLists)
    return data;
  }
}

// ค้นหา URL จากหมายเลขเครื่องตอก
function getSheetUrl(tabletID) {
  let ssMain = SpreadsheetApp.getActiveSpreadsheet();
  let shTabetList = ssMain.getSheetByName(globalVariables().shTabetList);

  let dataLists = shTabetList.getDataRange().getDisplayValues().slice(1);
  let datalist = dataLists.find(data => {
    return tabletID == data[0];
  });

  if (datalist) {
    let url = {
      url10s: datalist[3],
      urlIPC: datalist[5]
    }
    return url;
  }

  return null;
}

// ดึงข้อมูล Audit_trail รายละเอียดการปฏิบัติงาน
function getAuditTrail_data() {
  const verifyToken = validateToken();
  if (verifyToken.message === "success") {
    let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = spreadsheet.getSheetByName(globalVariables().shAudit_log);
    let data = sheet.getDataRange().getDisplayValues().slice(2);

    let dataObj = {}
    data.forEach((row) => {
      const timestamp = row[0];
      const rowData = {
        list: row[1],
        details: row[2],
        recorder: row[3],
        role: row[4],
      };

      // นำข้อมูลการชั่งแต่ล่ะครั้งไปเก็บใน dataObj
      dataObj[timestamp] = rowData;
    });

    console.log(dataObj)

    return dataObj;
  }
  else {
    return;
  }
};

// บันทึกการปฏิบัติงาน audit trail
function audit_trail(list, detail, username) {
  let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName(globalVariables().shAudit_log);
  let today = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Jakarta' });

  sheet.appendRow([today, list, detail, username]);
  sheet.getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns()).setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
}

// บันทึก remarks
function recordRemarks(form) {
  let spreadsheet = SpreadsheetApp.openByUrl(form.remarks_url);
  let sheet = spreadsheet.getSheetByName(globalVariables().shRemarks);
  let data = sheet.getDataRange().getDisplayValues();

  let dataList = [
    form.remark_timestamp,
    form.problem,
    form.causes,
    form.amendments,
    form.note,
    form.usernameLC
  ];

  // บันทึกการปฏิบัติงาน
  let auditTrial_msg = `ระบบเครื่องชั่ง ${form.remarks_type}\
                      \n${form.remarks_product}\
                      \n${form.remarks_lot}\
                      \nปัญหาที่พบ: ${form.problem}\
                      \nสาเหตุ: ${form.causes}\
                      \nการแก้ไข: ${form.amendments}\
                      \nหมายเหตุ: ${form.note}`;

  audit_trail("ลงบันทึก remarks", auditTrial_msg, form.usernameLC);

  for (let i = 2; i < data.length; i++) {
    if (data[i][0] == form.remark_timestamp) {
      sheet.getRange(i + 1, 1, 1, 6).setValues([dataList]);

      return { result: true, dataList };
    };
  };

  sheet.appendRow(dataList);
  sheet.getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns()).setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
  return { result: false, dataList };
}

// บันทึกการตั้งค่าน้ำหนัก
function setupWeight(form) {
  let url = getSheetUrl(form.TabletID_form);

  let ss10s = SpreadsheetApp.openByUrl(url.url10s);
  let sheet10s = ss10s.getSheetByName(globalVariables().shSetWeight);
  sheet10s.getRange(globalVariables().setupRange10s).setValues([
    [form.TabletID_form],
    [form.Balance10s_form],
    [form.ProductName_form],
    [form.Lot_form],
    [form.Weight10s_form],
    [form.Min10sControl_form],
    [form.Max10sControl_form],
    [form.MinDvt10s_form],
    [form.MaxDvt10s_form],
    [form.Percentage10s_form / 100],
    [form.MinThickness10s_form],
    [form.MaxThickness10s_form],
    [form.usernameLC],
    ["xxxxx"],
    ["xxxxx"]
  ]);

  sheet10s.getRange(globalVariables().setupRange10s).setNumberFormats([
    ['@'], ['@'], ['@'], ['@'],
    ['0.000'], ['0.000'], ['0.000'], ['0.000'], ['0.000'],
    ['0.00%'], ['0.00'], ['0.00'], ['@'], ['@'], ['@']
  ]);

  let ssIPC = SpreadsheetApp.openByUrl(url.urlIPC);
  let sheetIPC = ssIPC.getSheetByName(globalVariables().shSetWeight);
  let currentRange = sheetIPC.getRange("A3");
  if (currentRange.getDisplayValue() == "xxxxx") {
    currentRange.setValue("A19:B68");
  };

  sheetIPC.getRange(globalVariables().setupRangeIPC).setValues([
    [form.TabletID_form],
    [form.BalanceIPC_form],
    [form.ProductName_form],
    [form.NumberPastleIPC_form],
    [form.Lot_form],
    [form.NumberTabletsIPC_form],
    [form.WeightIPC_form],
    [form.PercentageIPC_form / 100],
    [form.MinAvgIPC_form],
    [form.MaxAvgIPC_form],
    [form.MinControlIPC_form],
    [form.MaxControlIPC_form],
    [form.MinDvtIPC_form],
    [form.MaxDvtIPC_form],
    [form.usernameLC],
    ["xxxxx"],
    ["xxxxx"]
  ]);

  sheetIPC.getRange(globalVariables().setupRangeIPC).setNumberFormats([
    ['@'], ['@'], ['@'], ['@'], ['@'], ['@'],
    ['0.000'], ['0.00%'],
    ['0.000'], ['0.000'], ['0.000'], ['0.000'], ['0.000'], ['0.000'], ['@'], ['@'], ['@']
  ]);

  // บันทึกการปฏิบัติงาน
  let detail = `\ชื่อยา: ${form.ProductName_form}\
                \nเลขที่ผลิต: ${form.Lot_form}\
                \nเครื่องตอก: ${form.TabletID_form}`;

  audit_trail("ตั้งค่าน้ำหนักยา", detail, form.usernameLC);

  const approval_msg = `🌈ขออนุมัติการตั้งค่าน้ำหนักยา
    \n🔰เครื่องตอก: ${form.TabletID_form}\
    \n🔰เลขที่ผลิต: ${form.Lot_form} \
    \n🔰ชื่อยา: ${form.ProductName_form} \
    \n⪼ กดลิงค์ด้านล่างเพื่อดำเนินการ \
    \n ${globalVariables().shortenedLinks}`;

  sendLineNotify(approval_msg, globalVariables().approval_token);

}

// แก้ไขฐานข้อมูลน้ำหนักยา
function addOrEditWeightDatabase(form) {
  let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName(globalVariables().shProductNameList);
  let producNameList = sheet.getDataRange().getDisplayValues();

  let dataLists = [
    form.ProductName_form,
    form.Weight10s_form,
    form.Percentage10s_form / 100,
    form.Min10sControl_form,
    form.Max10sControl_form,
    form.MinDvt10s_form,
    form.MaxDvt10s_form,
    form.MinThickness10s_form,
    form.MaxThickness10s_form,
    form.WeightIPC_form,
    form.PercentageIPC_form / 100,
    form.MinAvgIPC_form,
    form.MaxAvgIPC_form,
    form.MinDvtIPC_form,
    form.MaxDvtIPC_form,
    form.MinControlIPC_form,
    form.MaxControlIPC_form
  ];

  // บันทึกการปฏิบัติงาน
  let detail = `\ชื่อยา: ${form.ProductName_form}`;
  audit_trail("เพิ่ม/แก้ไข ฐานข้อมูลน้ำหนักยา", detail, form.usernameLC);

  for (let i = 2; i < producNameList.length; i++) {
    if (form.ProductName_form.toUpperCase() == producNameList[i][0].toUpperCase()) {
      sheet.getRange(i + 1, 1, 1, sheet.getLastColumn()).setValues([dataLists]);
      return dataLists;
    };
  };

  sheet.appendRow(dataLists);
  return dataLists;
}

// เพิ่มหรือแก้ไขรายชื่อพนักงาน
function addOrEditUser(form) {
  let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheetUsers = spreadsheet.getSheetByName(globalVariables().shUserList);
  let users = sheetUsers.getDataRange().getDisplayValues();

  let dataLists = [
    `'${form.rfid_input}`,
    form.employeeID_input,
    form.userNameTH_input,
    form.userNameEN,
    form.userPassword,
    form.userRoot
  ];

  // บันทึกการปฏิบัติงาน
  let detail = `\RFID: ${form.rfid_input}\
                \nรหัสพนักงาน: ${form.employeeID_input}\
                \nชื่อ-สกุล: ${form.userNameTH_input}\
                \nสิทธิการใช้งาน: ${form.userRoot}`;

  audit_trail("เพิ่ม/แก้ไข ข้อมูลผู้ใช้งาน", detail, form.usernameLC);

  for (let i = 2; i < users.length; i++) {
    if (form.rfid_input == users[i][0]) {
      sheetUsers.getRange(i + 1, 1, 1, 6).setValues([dataLists]);
      return dataLists;
    };
  };

  sheetUsers.appendRow(dataLists);
  return dataLists;
}

// ลบรายชื่อพนักงาน
function deleteUser(form) {
  let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheetUsers = spreadsheet.getSheetByName(globalVariables().shUserList);
  let users = sheetUsers.getDataRange().getDisplayValues();

  // บันทึกการปฏิบัติงาน
  let detail = `\RFID: ${form.rfid_input}\
                \nรหัสพนักงาน: ${form.employeeID_input}\
                \nชื่อ-สกุล: ${form.userNameTH_input}\
                \nสิทธิการใช้งาน: ${form.userRoot}`;

  for (let i = 2; i < users.length; i++) {
    if (form.rfid_input == users[i][0]) {
      sheetUsers.deleteRow(i + 1);
      audit_trail("ลบข้อมูลผู้ใช้งาน", detail, form.usernameLC); // บันทึกการปฏิบัติงาน
    };
  };
}
