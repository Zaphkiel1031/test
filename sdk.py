import streamlit as st
import streamlit.components.v1 as components

st.title("Coze Bot Integration")


gif_url = "https://raw.githubusercontent.com/j7808833/test_02/main/pic/Cyberpunk_bar_05.gif"
st.image(gif_url)


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
            bot_id: '7376255263235424257',  
          },
          componentProps: {
            title: 'Coze',  
            lang: 'zh-TW'  
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


components.html(html_code, height=600)