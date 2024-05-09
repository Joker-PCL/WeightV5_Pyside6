// ดึงข้อมูลชีตทั้งหมดที่อยู่ในฐานข้อมูล สร้าง dropdown list
function getProductionLists10s(jwtToken) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    const ssMain = SpreadsheetApp.getActiveSpreadsheet();
    const shTabetLists = ssMain.getSheetByName(globalVariables().shTabetLists);
    const shProductionLists = ssMain.getSheetByName(
      globalVariables().shProductionLists
    );
    const tabetLists = shTabetLists.getDataRange().getDisplayValues().slice(1);
    const productionLists = shProductionLists
      .getDataRange()
      .getDisplayValues()
      .slice(1);

    let sheetLists10s = [];

    if (verifyToken.userData.role != "Operator") {
      productionLists.forEach(([filename, type, sheetUrl, slidUrl]) => {
        if (type === "10S") {
          sheetLists10s.push({
            name: filename.toUpperCase(),
            url: sheetUrl,
            pdf: slidUrl.replace("edit?usp=drivesdk", "preview"),
          });
        }
      });
    }

    // จัดเรียงข้อมูลตามวันที่
    sheetLists10s = sheetLists10s.sort((item1, item2) => {
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
      const tablet_url_10s = data[3];
      sheetLists10s.push({
        name: `เครื่องตอก ${tablet_name} (LOT. ปัจจุบัน)`,
        url: tablet_url_10s,
        pdf: null,
      });
    });

    return { result: verifyToken, productionLists: sheetLists10s };
  }
}

// ดึงข้อมูลจากชีตปัจจุบัน จาก url ของชีต 10 เม็ด
function getWeighingData10s({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    // const url = "https://docs.google.com/spreadsheets/d/1XySGAC8aaywquHFKwr_zBBDpOgj99CF15UHe3P3kYF8/edit?usp=sharing"
    const spreadsheet = SpreadsheetApp.openByUrl(url); // เข้าถึง Spreadsheet
    const data_setting = spreadsheet
      .getSheetByName(globalVariables().shSetWeight) // เข้าถึง sheet ตั้งค่าน้ำหนักยา
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    const data_weighing = spreadsheet
      .getSheetByName(globalVariables().shWeight10s) // เข้าถึง sheet ชั่งน้ำหนัก
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(2); // ตัดข้อมูลส่วนหัวทิ้ง

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
      meanWeight: data_setting[4][1], // น้ำหนักตามทฤษฎี
      percentWeightVariation: data_setting[5][1], // เปอร์เซ็นเบี่ยงเบน
      meanWeightMin: data_setting[6][1], // ช่วงน้ำหนัก 10 เม็ด(Min.)
      meanWeightMax: data_setting[7][1], // ช่วงน้ำหนัก 10 เม็ด(Max.)
      meanWeightRegMin: data_setting[8][1], // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
      meanWeightRegMax: data_setting[9][1], // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
      thicknessMin: data_setting[10][1], // ค่าความหนา(Min.)
      thicknessMax: data_setting[11][1], // ค่าความหนา(Max.)
      prepared: data_setting[12][1], // ตั้งค่าน้ำหนักโดย
      approved: data_setting[13][1], // ตรวจสอบการตั้งค่าโดย
      finished: data_setting[14][1], // จบการผลิตโดย
      finishTime: data_setting[15][1], // จบการผลิตเวลา
    };

    // สร้างข้อมูลน้ำหนักยา
    let weighingData = [];
    data_weighing.forEach((row) => {
      const rowData = {
        timestamp: row[0],
        type: row[1],
        weight1: row[2],
        weight2: row[3],
        average: row[4],
        percent: row[5],
        characteristics: row[6],
        operator: row[7],
        inspector: row[8],
        thickness: [],
      };

      // ข้อมูลความหนา
      for (let i = 0; i < 10; i++) {
        rowData.thickness.push(row[9 + i]);
      }

      // นำข้อมูลการชั่งแต่ล่ะครั้งไปเก็บใน dataObj
      weighingData.push(rowData);
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

    // เก็บข้อมูลการชั่งน้ำหนักทั้งหมด
    const dataset = {
      settingDetail: settingDetail,
      weighingData: weighingData.reverse(),
      remarksData: remarksData.reverse(),
    };

    return { result: verifyToken, dataset: dataset };
  }
}

// ลงชื่อผู้ตรวจสอบการตั้งค่า
function signInToCheckTheSettings10s({ url, jwtToken }) {
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
      .getRange(globalVariables().approvedRange10s)
      .setValue(verifyToken.userData.nameTH);

    // สร้างข้อมูลการตั้งค่าน้ำหนักยา
    const settingDetail = {
      productName: data_setting[0][1], // ชื่อยา
      lot: data_setting[1][1], // เลขที่ผลิต
      tabletID: data_setting[3][1], // เครื่องตอก
    };

    // บันทึกการปฏิบัติงาน
    const details = `ระบบเครื่องชั่ง 10 เม็ด\
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
    const approval_msg = `🌈ระบบเครื่องชั่ง 10 เม็ด\n
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

// ลงชื่อผู้ตรวจสอบ
function signInToCheckTheWeighingData({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    const spreadsheet = SpreadsheetApp.openByUrl(url);
    const sheet = spreadsheet.getSheetByName(globalVariables().shWeight10s);
    const row = sheet.getLastRow();
    sheet
      .getRange(row, globalVariables().inspectorCol)
      .setValue(verifyToken.userData.nameTH);

    return { result: verifyToken, inspectorName: verifyToken.userData.nameTH };
  }
}

// สิ้นสุดการผลิต
function endOfProduction10s({ url, jwtToken }) {
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
      .getRange(globalVariables().finished10s)
      .setValue(verifyToken.userData.nameTH);
    shSetWeight.getRange(globalVariables().finishTime10s).setValue(today);

    // บันทึกการปฏิบัติงาน
    const productName = shSetWeight
      .getRange(globalVariables().finishRanges10s.productname)
      .getDisplayValue();
    const lot = shSetWeight
      .getRange(globalVariables().finishRanges10s.lot)
      .getDisplayValue();
    const tabletID = shSetWeight
      .getRange(globalVariables().finishRanges10s.tabletID)
      .getDisplayValue();

    const details = `ระบบเครื่องชั่ง: 10 เม็ด\
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
    const folder = DriveApp.getFolderById(globalVariables().folderId10s);
    const newSh = spreadsheet.copy(`${lot}_${productName}_${tabletID}_${date}`);
    const shUrl = newSh.getUrl(); // get newSheetID
    const shID = newSh.getId(); // get newSheetID
    const file = DriveApp.getFileById(shID);

    folder.addFile(file); // ย้ายไฟล์ไปยังแฟ้มเก็บข้อมูล

    // เคลียร์ข้อมูลชีตต้นฉบับ
    spreadsheet
      .getSheetByName(globalVariables().shWeight10s)
      .getRange(globalVariables().finishRanges10s.clearRanges.weighing)
      .clearContent();
    spreadsheet
      .getSheetByName(globalVariables().shRemarks)
      .getRange(globalVariables().finishRanges10s.clearRanges.remarks)
      .clearContent();
    spreadsheet
      .getSheetByName(globalVariables().shSetWeight)
      .getRange(globalVariables().setupRange10s)
      .setValue(globalVariables().finishRanges10s.clearRanges.settingText);

    return { result: verifyToken, urlCreatePDF: shUrl };
  }
}

// สร้างไฟล์ slide,pdf
function createPdf10s({ url, jwtToken }) {
  const getData = getWeighingData10s({ url: url, jwtToken: jwtToken });
  if (getData.result.message != "success") {
    return { result: getData.result };
  } else {
    const settingDetail = getData.dataset.settingDetail;
    const weighingData = getData.dataset.weighingData.reverse();
    const remarksData = getData.dataset.remarksData.reverse();

    // folder Slide
    const slideFolder = DriveApp.getFolderById(
      globalVariables().slideFolderId10s
    );

    // Templete SlideID
    const slideTemplate = DriveApp.getFileById(
      globalVariables().slideTemplateId10s
    );

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
    const chartSlide = slides[2];
    const weighingSlide = slides[3];

    // ดึงข้อมูล chart จากชีต, สร้างกราฟ
    const sheetChart = SpreadsheetApp.openByUrl(url);
    const chart = sheetChart
      .getSheetByName(globalVariables().shChart10s)
      .getCharts()[0];
    const chartWidth = globalVariables().chartSize.width;
    const chartHeight = globalVariables().chartSize.height;
    const chartTop = (newSlide.getPageHeight() - chartHeight) / 2;
    const chartLeft = (newSlide.getPageWidth() - chartWidth) / 2;
    chartSlide
      .insertSheetsChartAsImage(chart)
      .setWidth(chartWidth)
      .setHeight(chartHeight)
      .setTop(chartTop)
      .setLeft(chartLeft);

    newSlide.replaceAllText("{productname}", settingDetail.productName);
    newSlide.replaceAllText("{lot}", settingDetail.lot);
    newSlide.replaceAllText("{balanceID}", settingDetail.balanceID);
    newSlide.replaceAllText("{tabletID}", settingDetail.tabletID);
    newSlide.replaceAllText("{meanWeight}", settingDetail.meanWeight);
    newSlide.replaceAllText("{percent}", settingDetail.percentWeightVariation);
    newSlide.replaceAllText("{AVGmin}", settingDetail.meanWeightAvgMin);
    newSlide.replaceAllText("{AVGmax}", settingDetail.meanWeightAvgMax);
    newSlide.replaceAllText("{IHmin}", settingDetail.meanWeightInhouseMin);
    newSlide.replaceAllText("{IHmax}", settingDetail.meanWeightInhouseMax);
    newSlide.replaceAllText("{REGmin}", settingDetail.meanWeightRegMin);
    newSlide.replaceAllText("{REGmax}", settingDetail.meanWeightRegMax);
    newSlide.replaceAllText("{TKmin}", settingDetail.thicknessMin);
    newSlide.replaceAllText("{TKmax}", settingDetail.thicknessMax);
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

    const numRow = weighingSlide.getTables()[0].getNumRows() - 2;
    const totalPages = Math.ceil(weighingData.length / numRow);
    let totalWeight = [];
    let sumTotalWeight = 0;
    let totalThickness = [];
    let sumTotalThickness = 0;

    for (let page = 0; page < totalPages; page++) {
      let slide;
      if (page == totalPages - 1) {
        slide = weighingSlide;
      } else {
        slide = weighingSlide.duplicate();
      }

      const table = slide.getTables()[0];
      slide.move(newSlide.getSlides().length);
      for (let row = 0; row < numRow; row++) {
        const dataLength = numRow * page + row;
        const currentRow = row + 2;
        if (dataLength < weighingData.length) {
          const dataset = weighingData[dataLength];
          const timestampCell = table.getRow(currentRow).getCell(0);
          const weight1Cell = table.getRow(currentRow).getCell(1);
          const weight2Cell = table.getRow(currentRow).getCell(2);
          const averageCell = table.getRow(currentRow).getCell(3);
          const percentCell = table.getRow(currentRow).getCell(4);
          const characteristicsCell = table.getRow(currentRow).getCell(5);
          const operatorCell = table.getRow(currentRow).getCell(16);
          const inspectorCell = table.getRow(currentRow).getCell(17);

          timestampCell.getText().setText(dataset.timestamp);
          weight1Cell.getText().setText(dataset.weight1);
          weight2Cell.getText().setText(dataset.weight2);
          averageCell.getText().setText(dataset.average);
          percentCell.getText().setText(`${dataset.percent}%`);
          characteristicsCell.getText().setText(dataset.characteristics);
          operatorCell.getText().setText(dataset.operator);
          inspectorCell.getText().setText(dataset.inspector);

          if (
            parseFloat(dataset.weight1) >=
              parseFloat(settingDetail.meanWeightRegMin) &&
            parseFloat(dataset.weight1) <=
              parseFloat(settingDetail.meanWeightRegMax) &&
            parseFloat(dataset.weight2) >=
              parseFloat(settingDetail.meanWeightRegMin) &&
            parseFloat(dataset.weight2) <=
              parseFloat(settingDetail.meanWeightRegMax)
          ) {
            totalWeight.push(parseFloat(dataset.weight1));
            totalWeight.push(parseFloat(dataset.weight2));
            sumTotalWeight += parseFloat(dataset.weight1);
            sumTotalWeight += parseFloat(dataset.weight2);
          }

          dataset.thickness.forEach((thickness, index) => {
            const thicknessCell = table.getRow(currentRow).getCell(index + 6);
            thicknessCell.getText().setText(thickness);
            if (
              thickness != "-" ||
              (parseFloat(thickness) >=
                parseFloat(settingDetail.meanWeightRegMin) &&
                parseFloat(thickness) <=
                  parseFloat(settingDetail.meanWeightRegMax))
            ) {
              totalThickness.push(parseFloat(thickness));
              sumTotalThickness += parseFloat(thickness);
            }
          });

          if (dataLength == 0) {
            detailSlide.replaceAllText("{startTime}", dataset.timestamp);
          }
        } else {
          break;
        }
      }
    }

    detailSlide.replaceAllText(
      "{sumWTmin}",
      Math.min(...totalWeight).toFixed(3)
    );
    detailSlide.replaceAllText(
      "{sumWTmax}",
      Math.max(...totalWeight).toFixed(3)
    );
    detailSlide.replaceAllText(
      "{sumWTavg}",
      (sumTotalWeight / totalWeight.length).toFixed(3)
    );

    detailSlide.replaceAllText(
      "{sumTKmin}",
      Math.min(...totalThickness).toFixed(2)
    );
    detailSlide.replaceAllText(
      "{sumTKmax}",
      Math.max(...totalThickness).toFixed(2)
    );
    detailSlide.replaceAllText(
      "{sumTKavg}",
      (sumTotalThickness / totalThickness.length).toFixed(2)
    );

    const mainSpreadSheet = SpreadsheetApp.getActiveSpreadsheet();
    const mainProductionLists = mainSpreadSheet.getSheetByName(
      globalVariables().shProductionLists
    );
    mainProductionLists.appendRow([
      SpreadsheetApp.openByUrl(url).getName(),
      "10S",
      url,
      newSlideCopy.getUrl(),
    ]);

    return { result: getData.result };
  }
}
