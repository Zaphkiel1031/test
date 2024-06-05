import streamlit as st
import streamlit.components.v1 as components

st.title("Coze Bot Integration")

# 嵌入HTML和JavaScript代码
html_code = """
<!DOCTYPE html>
<html>
<head>
  <title>Coze Bot Integration</title>
  <script src="https://sf-cdn.coze.com/obj/unpkg-va/flow-platform/chat-app-sdk/0.1.0-beta.2/libs/oversea/index.js"></script>
</head>
<body>
  <div id="coze-chat"></div>
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      try {
        new CozeWebSDK.WebChatClient({
          config: {
            bot_id: '7355203240146829328',  // 替换为你的Bot ID
          },
          componentProps: {
            title: 'Coze',  // 聊天组件的标题
          },
        });
        console.log("Coze Web SDK initialized successfully.");
      } catch (error) {
        console.error("Error initializing Coze Web SDK:", error);
        document.getElementById("coze-chat").innerText = "Error initializing Coze Web SDK: " + error.message;
      }
    });
  </script>
</body>
</html>
"""

# 使用Streamlit的HTML组件嵌入代码
components.html(html_code, height=600)