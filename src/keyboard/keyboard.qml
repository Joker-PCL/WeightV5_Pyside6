import QtQuick 2.15
import QtQuick.VirtualKeyboard 2.1

Rectangle {
    width: 800
    height: 400
    color: "lightgray"

    InputPanel {
        id: inputPanel
        anchors.fill: parent
        visible: true

        Component.onCompleted: {
            inputPanel.active = true
            Qt.inputMethod.show()
        }
    }
}
