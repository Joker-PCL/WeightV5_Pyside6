// ตั้งค่า
function globalVariables() {
  const Variables = {
    // icon https://pic.in.th/
    icon: "https://img5.pic.in.th/file/secure-sv1/table-of-content.png",

    // MetaTag
    metaTag06: ['viewport', 'width=device-width, height=device-height,initial-scale=0.6, minimum-scale=0.6, maximum-scale=0.6'],
    metaTag08: ['viewport', 'width=device-width, height=device-height,initial-scale=0.8, minimum-scale=0.8, maximum-scale=0.8'],
    // Shortened links
    shortenedLinks: "https://bit.ly/WeightTableV4",
    // Line token
    alert_token: "p9YWBiZrsUAk7Ef9d0hLTMMF2CxIaTnRopHaGcosM4q",
    approval_token: "lYlhqcenm4d8Vq4VJOYO2T8VHh0tbaW7oSrsJU9tm7f",

    // แฟ้มข้อมูลเวอร์ชั่นเก่า
    folderIdIPC_OLD: "1RJx8vxspQTJR05GaTLtLqm1kBtfQYC0W",
    folderId10s_OLD: "10JT2s9zd8pcmSj-kB2T5s-kFHlW58IE3",

    // ข้อมูลใน Main_Setup
    shUserList: "User_Password",      // ชีตข้อมูลรายชื่อพนักงาน
    shTabetList: "TabletID",          // ข้อมูล url เครื่องตอก
    shScaleList: "ScaleID",           // ชีตข้อมูลเครื่องชั่ง
    shProductNameList: "ProductNameList",   // ชีตข้อมูลรายชื่อยา
    shAudit_log: "Audit_Log",         // ชีต audit trail

    shRemarks: "Remark",          // ชีต Remarks 
    shSetWeight: "Setting",        // ชีต ข้อมูลการตั้งค่าน้ำหนัก

    // ข้อมูลของระบบชั่ง 10 เม็ด
    folderId10s: "1J7jfGUshmFox9RHK2cqfvCGTaQcncOKx",  // ID โฟล์เดอร์แฟ้มข้อมูลน้ำหนัก 10 เม็ด
    shWeight10s: "WEIGHT",           // ข้อมูลน้ำหนัก 10 เม็ด
    setupRange10s: "A2:A16",         // ตำแหน่ง ข้อมูลการตั้งค่าน้ำหนัก 10 เม็ด
    checkSetupRange10s: "A15",       // ตำแหน่ง ลงชื่อตรวจสอบการตั้งค่าน้ำหนัก 10 เม็ด
    checkEndjobRange10s: "A16",       // ตำแหน่ง ลงชื่อ endjob การตั้งค่าน้ำหนัก 10 เม็ด

    // ข้อมูลระบบชั่ง IPC
    folderIdIPC: "1qtpt0eAp_IOWe1BEh-x75nM5FXNy9tdW",  // ID โฟล์เดอร์แฟ้มข้อมูล IPC
    shWeightIPC: "Weight",  // ข้อมูลน้ำหนัก IPC
    setupRangeIPC: "A4:A20",          // ตำแหน่ง ข้อมูลการตั้งค่าน้ำหนัก IPC
    checkSetupRangeIPC: "A19",       // ตำแหน่ง ลงชื่อตรวจสอบการตั้งค่าน้ำหนัก IPC
    checkEndjobRangeIPC: "A20",       // ตำแหน่ง ลงชื่อ endjob การตั้งค่าน้ำหนัก IPC
    summaryRecordRangeIPC: "G2:G4",   // ตำแหน่ง สรุปผลน้ำหนัก IPC
    dataRangeIPC: ["A17:B68", "D17:E68", "G17:H68", "J17:K68"],      // ตำแหน่ง ข้อมูลการน้ำหนัก IPC
    summaryRangeIPC: ["A69:B78", "D69:E78", "G69:H78", "J69:K78"],   // ตำแหน่ง ข้อมูลการน้ำหนัก IPC
    timestampRangeIPC: ["A17", "D17", "G17", "J17"], // ตำแหน่งบันทึกเวลา IPC
    tabletDetailRangeIPC: ["B73", "E73", "H73", "K73"] // ตำแหน่งรายละเอียดเม็ดยา IPC
  }

  return Variables;
}

function doGet(e) {
  const verifyToken = validateToken();
  if (verifyToken.message === "success") {
    let htmlOutput = HtmlService.createTemplateFromFile('Index');
    htmlOutput.username = verifyToken.data.nameTH;
    htmlOutput.role = verifyToken.data.role;
    return htmlOutput.evaluate()
      .setFaviconUrl(globalVariables().icon)
      .addMetaTag(...globalVariables().metaTag06)
      .setTitle("Weight Table")
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
  } else {
    let htmlOutput = HtmlService.createTemplateFromFile('Login');
    htmlOutput.username = "";
    htmlOutput.message1 = "";
    htmlOutput.message2 = "";
    return htmlOutput.evaluate()
      .setFaviconUrl(globalVariables().icon)
      .addMetaTag(...globalVariables().metaTag08)
      .setTitle("Login")
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
  }
}

function doPost(e) {
  if (e.parameters) {
    if (e.parameters.logout) {
      return logout();
    }

    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = spreadsheet.getSheetByName(globalVariables().shUserList);
    const dataLists = sheet.getDataRange().getDisplayValues().slice(2);

    if (e.parameters.username && e.parameters.password) {
      const results = dataLists.find(dataList => {
        const _username = dataList[2];
        return _username == e.parameters.username;
      });

      if (results) {
        const privateKey = sha256(`${e.parameters.password}`);
        const [_rfid, _id, _nameTH, _nameEN, _privateKey, _role] = results;
        const data = {
          "nameTH": _nameTH,
          "nameEN": _nameEN,
          "role": _role
        }

        if (_privateKey == privateKey) {
          const token = generateAccessToken({ privateKey, data });
          setCookie(token, privateKey);

          const template = HtmlService.createTemplateFromFile('Index');
          template.username = _nameTH;
          template.role = _role;
          return template.evaluate()
            .setFaviconUrl(globalVariables().icon)
            .addMetaTag(...globalVariables().metaTag06)
            .setTitle("Weight Table")
            .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
        }
        else {
          const template = HtmlService.createTemplateFromFile('Login');
          template.username = e.parameters.username;
          template.message1 = "";
          template.message2 = "*รหัสผ่านไม่ถูกต้อง";
          return template.evaluate()
            .setFaviconUrl(globalVariables().icon)
            .addMetaTag(...globalVariables().metaTag08)
            .setTitle("Login")
            .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
        }
      }
      else {
        const template = HtmlService.createTemplateFromFile('Login');
        template.username = e.parameters.username;
        template.message1 = "*ไม่พบข้อมูลผู้ใช้งาน";
        template.message2 = "";
        return template.evaluate()
          .setFaviconUrl(globalVariables().icon)
          .addMetaTag(...globalVariables().metaTag08)
          .setTitle("Login")
          .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
      }
    }
  }
}

function logout() {
  clearCookie();
  let htmlOutput = HtmlService.createTemplateFromFile('Login');
  htmlOutput.username = "";
  htmlOutput.message1 = "";
  htmlOutput.message2 = "";
  return htmlOutput.evaluate()
    .setFaviconUrl(globalVariables().icon)
    .addMetaTag(...globalVariables().metaTag08)
    .setTitle("Login")
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// ตรวจสอบข้อมูลผู้ใช้งานจาก LoginForm
function authentication(username, password) {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = spreadsheet.getSheetByName(globalVariables().shUserList);
  const user_data = sheet.getDataRange().getDisplayValues().slice(2);

  const search_user = user_data.find((data) => {
    const _username = data[2];
    return username == _username;
  });

  if (search_user) {
    const data = {
      nameTH: search_user[2],
      nameEN: search_user[3],
      role: search_user[5]
    }

    const search_user_password = search_user[4];

    if (search_user_password == password) {
      // สร้าง token
      const token = generateAccessToken({ privateKey: password, data });
      return { message: "success", token };
    }
    else {
      return { message: "password is incorrect!" };
    }
  }
  else {
    return { message: "no user information found!!" };
  };
};

//********* ส่งไลน์
function sendLineNotify(message, token) {
  if (!token) {
    token = globalVariables().alert_token;
  }

  var options = {
    "method": "post",
    "payload": "message=" + message,
    "headers": {
      "Authorization": "Bearer " + token
    }
  };

  UrlFetchApp.fetch("https://notify-api.line.me/api/notify", options);
}

function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

function getUrl() {
  const url = ScriptApp.getService().getUrl();
  return url;
}






