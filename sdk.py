import streamlit as st
import streamlit.components.v1 as components

st.title("Coze Bot Integration")

# 显示GIF图片
gif_url = "https://raw.githubusercontent.com/j7808833/test_02/main/pic/Cyberpunk_bar_05.gif"
st.image(gif_url)

# 嵌入HTML和JavaScript代码
html_code = """
<!DOCTYPE html>
<html>
<head>
  <title>Coze Bot Integration</title>
  <style>
    #coze-chat {
      width: 100%;
      height: 600px;
      border: 1px solid #ccc;
    }
  </style>
  <script src="https://sf-cdn.coze.com/obj/unpkg-va/flow-platform/chat-app-sdk/0.1.0-beta.2/libs/oversea/index.js"></script>
</head>
<body>
  <div id="coze-chat"></div>
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      try {
        new CozeWebSDK.WebChatClient({
          config: {
            bot_id: '7376255263235424257',  // 替换为你的Bot ID
          },
          componentProps: {
            title: 'Coze',  // 聊天组件的标题
            containerId: 'coze-chat',  // 将聊天组件嵌入到指定的div中
            width: '100%',  // 设置聊天组件的宽度
            height: '600px'  // 设置聊天组件的高度
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
