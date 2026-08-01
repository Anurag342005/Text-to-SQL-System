from sql.generator import generate_sql
from sql.executor import execute_sql
from llm.explainer import explain_result

import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

# ---------------------- SESSION STATE ---------------------- #

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------------- PAGE CONFIG ---------------------- #

st.set_page_config(
    page_title="Text-to-SQL Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------- SIDEBAR CHAT HISTORY ---------------------- #

with st.sidebar:

    st.header("📜 Chat History")

    if len(st.session_state.chat_history) == 0:
        st.info("No previous chats")

    else:

        for i, chat in enumerate(
            st.session_state.chat_history[::-1]
        ):

            st.write(f"### Chat {len(st.session_state.chat_history)-i}")

            st.write("**Question:**")
            st.write(chat["question"])

            st.write("**SQL:**")
            st.code(
                chat["sql"],
                language="sql"
            )

            st.divider()


    if st.button("🗑 Clear History"):

        st.session_state.chat_history = []
        st.rerun()

# ---------------------- CSS ---------------------- #

st.markdown("""
<style>

/* Main container */
.block-container{
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* H1 (Title) */
h1{
    text-align: center;
    margin-bottom: 0.2rem !important;
}

/* Paragraph below title */
div[data-testid="stMarkdownContainer"] p{
    text-align: center;
    margin-top: 0 !important;
    margin-bottom: 0.2rem !important;
}

/* Divider */
hr{
    margin-top: 0.3rem !important;
    margin-bottom: 0.8rem !important;
}

/* Reduce space before widgets */
div[data-testid="stVerticalBlock"] > div{
    padding-top: 0rem;
}

/* Button */
.stButton > button{
    width: 100%;
    height: 45px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ---------------------- #

st.title("🤖 Text-to-SQL Assistant")

st.write(
    "Convert Natural Language into SQL Queries using LLMs, SQLite, LangChain and Groq."
)

st.divider()

# ---------------------- INPUT ---------------------- #
st.markdown("### Ask your question")
question = st.text_input(
    "",
    placeholder="Example: Show employees whose salary is greater than 70000",
    label_visibility="collapsed"
)
generate = st.button("🚀 Generate SQL")

# ---------------------- MAIN ---------------------- #

if generate:

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Generating SQL..."):

        sql = generate_sql(question)

    st.subheader("Generated SQL")

    st.code(sql, language="sql")
    # ---------------- DOWNLOAD SQL ---------------- #

    st.download_button(
        label="⬇️ Download SQL",
        data=sql,
        file_name="generated_query.sql",
        mime="text/sql"
    )

    result = execute_sql(sql)

    if result["success"]:

        df = result["data"]

        st.subheader("Query Result")

        # ---------- Center Align ---------- #

        cell_style = JsCode("""
        function(params) {
            return {
                'textAlign': 'center',
                'display':'flex',
                'justifyContent':'center',
                'alignItems':'center'
            }
        }
        """)

        header_style = JsCode("""
        function(params){
            return {
                'justifyContent':'center',
                'fontWeight':'bold'
            }
        }
        """)

        gb = GridOptionsBuilder.from_dataframe(df)

        for col in df.columns:

            gb.configure_column(
                col,
                cellStyle=cell_style,
                headerClass="ag-center-aligned-header"
            )

        gridOptions = gb.build()
        height = 45 + (len(df) * 38)

        AgGrid(
            df,
            gridOptions=gridOptions,
            theme="streamlit",
            height=height,
            fit_columns_on_grid_load=True,
            allow_unsafe_jscode=True,
            custom_css={
                ".ag-header-cell-label": {
                    "justify-content": "center !important"
                },
                ".ag-header-cell-text": {
                    "width": "100%",
                    "text-align": "center !important",
                    "font-weight": "bold"
                },
                ".ag-cell": {
                    "text-align": "center !important"
                }
            }
        )

        # ---------------- DOWNLOAD QUERY RESULT ---------------- #

        csv = df.to_csv(index=False)

        st.download_button(
            label="⬇️ Download Result CSV",
            data=csv,
            file_name="query_result.csv",
            mime="text/csv"
        )

        with st.spinner("Generating AI Answer..."):

            answer = explain_result(question, df)

        st.subheader("Final Answer")

        st.success(answer)
        # Save Chat History

        st.session_state.chat_history.append(
            {
                "question": question,
                "sql": sql,
                "answer": answer
            }
        )

    else:

        st.error(result["error"])