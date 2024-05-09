// ดึงข้อมูล Main_Setup สำหรับการตั้งค่าทั้งหมด
function getDataSetting(jwtToken) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheetUsers = spreadsheet.getSheetByName(
      globalVariables().shUserLists
    );
    const sheetTablet = spreadsheet.getSheetByName(
      globalVariables().shTabetLists
    );
    const sheetScale = spreadsheet.getSheetByName(
      globalVariables().shBalanceLists
    );
    const sheetProductName = spreadsheet.getSheetByName(
      globalVariables().shWeighingSettings
    );

    const userDataLists = sheetUsers.getDataRange().getDisplayValues().slice(2);
    const tabletDataLists = sheetTablet
      .getDataRange()
      .getDisplayValues()
      .slice(1);
    const balanceDataLists = sheetScale
      .getDataRange()
      .getDisplayValues()
      .slice(1);
    const productNameDataLists = sheetProductName
      .getDataRange()
      .getDisplayValues()
      .slice(2);

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
        url_10s: row[3],
        url_ipc: row[4],
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
      const dataList = {};
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
        thickness10sMax: row[8],
      };

      const weight_control_ipc = {
        meanWeightIpc: row[9],
        percentWeightVariationIpc: row[10],
        meanWeightAverageIpcMin: row[11],
        meanWeightAverageIpcMax: row[12],
        meanWeightVariationIpcMin: row[13],
        meanWeightVariationIpcMax: row[14],
        meanWeightRegIpcMin: row[15],
        meanWeightRegIpcMax: row[16],
      };

      // เพิ่มข้อมูล user_data_list ไปยัง userList
      dataList["weight_control_10s"] = weight_control_10s;
      dataList["weight_control_ipc"] = weight_control_ipc;

      productLists[productName] = dataList;
    });

    const dataSettings = {
      userLists: userLists,
      tabletLists: tabletLists,
      balanceLists: balanceLists,
      productLists: productLists,
    };

    return { result: verifyToken, dataSettings: dataSettings };
  }
}

// ดึงข้อมูลผู้ใช้งาน
function getUserDataLists(jwtToken) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheetUsers = spreadsheet.getSheetByName(
      globalVariables().shUserLists
    );
    
    const userDataLists = sheetUsers
      .getDataRange()
      .getDisplayValues()
      .slice(2);

    /** สร้างข้อมูลรายชื่อผู้ใช้งาน **/
    let userLists = []; // สร้าง data object เก็บข้อมูล
    userDataLists.forEach((row) => {
      userLists.push({
        rfid: row[0],
        employeeId: row[1],
        usernameTH: row[2],
        usernameEN: row[3],
        role: row[5],
      });
    });

    userLists.sort((a, b) => a.usernameTH.localeCompare(b.usernameTH, 'th'));

    return { result: verifyToken, userDataLists: userLists };
  }
}

// ดึงข้อมูล Audit trail รายละเอียดการปฏิบัติงาน
function getAuditTrailData(jwtToken) {
  const verifyToken = validateToken(jwtToken);
  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = spreadsheet.getSheetByName(globalVariables().shAuditLog);
    let dataset = sheet.getDataRange().getDisplayValues().slice(1).reverse();

    return { result: verifyToken, dataset: dataset };
  }
}

// บันทึกการปฏิบัติงาน audit trail
function recordAuditTrailData({ list, details, username, role }) {
  let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = spreadsheet.getSheetByName(globalVariables().shAuditLog);
  let timestamp = new Date().toLocaleString("en-GB", {
    timeZone: "Asia/Bangkok",
  });

  sheet.appendRow([timestamp, list, details, username, role]);
  sheet
    .getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns())
    .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
}

// ค้นหา URL จากหมายเลขเครื่องตอก
function getSheetUrl(tabletID) {
  let ssMain = SpreadsheetApp.getActiveSpreadsheet();
  let shTabetLists = ssMain.getSheetByName(globalVariables().shTabetLists);

  let dataLists = shTabetLists.getDataRange().getDisplayValues().slice(1);
  let datalist = dataLists.find((data) => {
    return tabletID == data[0];
  });

  if (datalist) {
    let url = {
      url10s: datalist[3],
      urlIPC: datalist[5],
    };
    return url;
  }

  return null;
}

// บันทึก remarks
function recordRemarksData({ url, form, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    const spreadsheet = SpreadsheetApp.openByUrl(url);
    const sheet = spreadsheet.getSheetByName(globalVariables().shRemarks);
    const data = sheet.getDataRange().getDisplayValues();

    const data_setting = spreadsheet
      .getSheetByName(globalVariables().shSetWeight) // เข้าถึง sheet ตั้งค่าน้ำหนักยา
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    // สร้างข้อมูลการตั้งค่าน้ำหนักยา
    const settingDetail = {
      productName: data_setting[0][1], // ชื่อยา
      lot: data_setting[1][1], // เลขที่ผลิต
      tabletID: data_setting[3][1], // เครื่องตอก
    };

    const details = [
      form.timestamp,
      form.issues,
      form.cause,
      form.resolves,
      verifyToken.userData.nameTH,
      verifyToken.userData.role,
    ];

    // บันทึกการปฏิบัติงาน
    let auditTrial_msg = `ระบบเครื่องชั่ง ${form.type}\
                      \nnชื่อยา ${settingDetail.productName}\
                      \nnเลขที่ผลิต ${settingDetail.lot}\
                      \nปัญหาที่พบ: ${form.issues}\
                      \nสาเหตุ: ${form.cause}\
                      \nการแก้ไข: ${form.resolves}`;

    recordAuditTrailData({
      list: "ลงบันทึก remarks",
      details: auditTrial_msg,
      username: verifyToken.userData.nameTH,
      role: verifyToken.userData.role,
    });

    for (let i = 1; i < data.length; i++) {
      if (data[i][0] == form.timestamp) {
        sheet.getRange(i + 1, 1, 1, sheet.getMaxColumns()).setValues([details]);

        return { result: verifyToken, details: details };
      }
    }

    sheet.appendRow(details);
    sheet
      .getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns())
      .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
    return { result: verifyToken, details: details };
  }
}

// บันทึกการตั้งค่าน้ำหนัก
function setupWeight({ form, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    let url = getSheetUrl(form.tabletID);

    let ss10s = SpreadsheetApp.openByUrl(url.url10s);
    let sheet10s = ss10s.getSheetByName(globalVariables().shSetWeight);
    sheet10s
      .getRange(globalVariables().setupRange10s)
      .setValues([
        [form.productName],
        [form.lot],
        [form.balanceId10s],
        [form.tabletID],
        [form.meanWeight10s],
        [form.percentWeightVariation10s / 100],
        [form.meanWeight10sMin],
        [form.meanWeight10sMax],
        [form.meanWeightReg10sMin],
        [form.meanWeightReg10sMax],
        [form.thickness10sMin],
        [form.thickness10sMax],
        [verifyToken.userData.nameTH],
        ["xxxxx"],
        ["xxxxx"],
        ["xxxxx"],
      ]);

    sheet10s
      .getRange(globalVariables().setupRange10s)
      .setNumberFormats([
        ["@"],
        ["@"],
        ["@"],
        ["@"],
        ["0.000"],
        ["0.00%"],
        ["0.000"],
        ["0.000"],
        ["0.000"],
        ["0.000"],
        ["0.00"],
        ["0.00"],
        ["@"],
        ["@"],
        ["@"],
        ["@"],
      ]);

    let ssIPC = SpreadsheetApp.openByUrl(url.urlIPC);
    let sheetIPC = ssIPC.getSheetByName(globalVariables().shSetWeight);
    let currentRange = sheetIPC.getRange("A3");
    if (currentRange.getDisplayValue() == "xxxxx") {
      currentRange.setValue("A19:B68");
    }

    sheetIPC
      .getRange(globalVariables().setupRangeIPC)
      .setValues([
        [form.productName],
        [form.lot],
        [form.balanceIdIpc],
        [form.tabletID],
        [form.numberPunches],
        [form.numberTablets],
        [form.meanWeightIpc],
        [form.percentWeightVariationIpc / 100],
        [form.meanWeightAverageIpcMin],
        [form.meanWeightAverageIpcMax],
        [form.meanWeightVariationIpcMin],
        [form.meanWeightVariationIpcMax],
        [form.meanWeightRegIpcMin],
        [form.meanWeightRegIpcMax],
        [verifyToken.userData.nameTH],
        ["xxxxx"],
        ["xxxxx"],
        ["xxxxx"],
      ]);

    sheetIPC
      .getRange(globalVariables().setupRangeIPC)
      .setNumberFormats([
        ["@"],
        ["@"],
        ["@"],
        ["@"],
        ["@"],
        ["@"],
        ["0.000"],
        ["0.00%"],
        ["0.000"],
        ["0.000"],
        ["0.000"],
        ["0.000"],
        ["0.000"],
        ["0.000"],
        ["@"],
        ["@"],
        ["@"],
        ["@"],
      ]);

    // บันทึกการปฏิบัติงาน
    let details = `\ชื่อยา: ${form.productName}\
                \nเลขที่ผลิต: ${form.lot}\
                \nเครื่องตอก: ${form.tabletID}`;

    recordAuditTrailData({
      list: "ตั้งค่าน้ำหนักยา",
      details: details,
      username: verifyToken.userData.nameTH,
      role: verifyToken.userData.role,
    });

    const approval_msg = `🌈ขออนุมัติการตั้งค่าน้ำหนักยา
    \n🔰เครื่องตอก: ${form.productName}\
    \n🔰เลขที่ผลิต: ${form.lot} \
    \n🔰ชื่อยา: ${form.tabletID} \
    \n⪼ กดลิงค์ด้านล่างเพื่อดำเนินการ \
    \n ${globalVariables().shortenedLinks}`;

    sendLineNotify(approval_msg, globalVariables().approvalToken);

    return { result: verifyToken };
  }
}

// แก้ไขฐานข้อมูลน้ำหนักยา
function addOrEditWeightDatabase({ form, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = spreadsheet.getSheetByName(
      globalVariables().shWeighingSettings
    );
    let productLists = sheet.getDataRange().getDisplayValues();

    let dataLists = [
      form.productName,
      form.meanWeight10s,
      form.percentWeightVariation10s / 100,
      form.meanWeight10sMin,
      form.meanWeight10sMax,
      form.meanWeightReg10sMin,
      form.meanWeightReg10sMax,
      form.thickness10sMin,
      form.thickness10sMax,
      form.meanWeightIpc,
      form.percentWeightVariationIpc / 100,
      form.meanWeightAverageIpcMin,
      form.meanWeightAverageIpcMax,
      form.meanWeightVariationIpcMin,
      form.meanWeightVariationIpcMax,
      form.meanWeightRegIpcMin,
      form.meanWeightRegIpcMax,
    ];

    // บันทึกการปฏิบัติงาน
    let details = `\ชื่อยา: ${form.productName}`;
    recordAuditTrailData({
      list: "เพิ่ม/แก้ไข ฐานข้อมูลน้ำหนักยา",
      details: details,
      username: verifyToken.userData.nameTH,
      role: verifyToken.userData.role,
    });

    for (let i = 2; i < productLists.length; i++) {
      if (form.productName.toUpperCase() == productLists[i][0].toUpperCase()) {
        sheet
          .getRange(i + 1, 1, 1, sheet.getLastColumn())
          .setValues([dataLists]);
        return {
          result: verifyToken,
          productLists: getDataSetting(jwtToken).dataSettings.productLists,
        };
      }
    }

    sheet.appendRow(dataLists);
    return {
      result: verifyToken,
      productLists: getDataSetting(jwtToken).dataSettings.productLists,
    };
  }
}

// เพิ่มหรือแก้ไขรายชื่อพนักงาน
function addOrEditUserData({ form, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    let sheetUsers = spreadsheet.getSheetByName(globalVariables().shUserLists);
    let users = sheetUsers.getDataRange().getDisplayValues();

    let dataLists = [
      `'${form.rfid}`,
      form.employeeId,
      form.usernameTH,
      form.usernameEN,
      sha256(form.password),
      form.role,
    ];

    // บันทึกการปฏิบัติงาน
    let details = `\RFID: ${form.rfid}\
                \nรหัสพนักงาน: ${form.employeeId}\
                \nชื่อ-สกุล: ${form.usernameTH}\
                \nสิทธิการใช้งาน: ${form.role}`;

    recordAuditTrailData({
      list: "เพิ่ม/แก้ไข ข้อมูลผู้ใช้งาน",
      details: details,
      username: verifyToken.userData.nameTH,
      role: verifyToken.userData.role,
    });

    for (let i = 2; i < users.length; i++) {
      const rfid = users[i][0];
      if (form.rfid == rfid) {
        sheetUsers.getRange(i + 1, 1).setValue(`'${form.rfid}`);
        sheetUsers.getRange(i + 1, 2).setValue(form.employeeId);
        sheetUsers.getRange(i + 1, 3).setValue(form.usernameTH);
        sheetUsers.getRange(i + 1, 4).setValue(form.usernameEN);
        if (form.password) {
          sheetUsers.getRange(i + 1, 5).setValue(sha256(form.password));
        }
        sheetUsers.getRange(i + 1, 6).setValue(form.role);
        return { result: verifyToken };
      }
    }

    sheetUsers.appendRow(dataLists);
    return { result: verifyToken };
  }
}

// ลบรายชื่อพนักงาน
function deleteUser({ form, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message !== "success") {
    return { result: verifyToken };
  } else {
    let spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    let sheetUsers = spreadsheet.getSheetByName(globalVariables().shUserLists);
    let users = sheetUsers.getDataRange().getDisplayValues();

    // บันทึกการปฏิบัติงาน
    let details = `\RFID: ${form.rfid}\
                \nรหัสพนักงาน: ${form.employeeId}\
                \nชื่อ-สกุล: ${form.usernameTH}\
                \nสิทธิการใช้งาน: ${form.role}`;

    for (let i = 2; i < users.length; i++) {
      const rfid = users[i][0];
      if (form.rfid == rfid) {
        sheetUsers.deleteRow(i + 1);
        recordAuditTrailData({
          list: "ลบข้อมูลผู้ใช้งาน",
          details: details,
          username: verifyToken.userData.nameTH,
          role: verifyToken.userData.role,
        });

        return { result: verifyToken };
      }
    }
  }
}
