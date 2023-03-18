import streamlit as st 

# 2. Text Element

st.title("Text Element")

#st.markdown
st.subheader("Markdown")

st.markdown("Display string formatted as Markdown")
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :purple[colored purple], and this is **:blue[colored]** and bold.")
st.markdown(":pencil: :green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity.")

#st.title
st.subheader("Title")

st.title("Display text in title formatting")
st.title('This is a title')
st.title('A title with _italics_ :purple[colors] and emojis :sunglasses:')

#st.header
st.subheader("Header")

st.header('This is a header')
st.header('A header with _italics_ :purple[colors] and emojis :sunglasses:')

#st.subheader
st.subheader("Subheader")

st.subheader('This is a subheader')
st.subheader('A subheader with _italics_ :purple[colors] and emojis :sunglasses:')

#st.caption
st.subheader("Caption")

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :purple[colors] and emojis :sunglasses:')

#st.code
st.subheader("Code block")

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

#st.text
st.subheader("Preformatted text")

st.text('This is some text.')

#st.latex
st.subheader("Latex")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

