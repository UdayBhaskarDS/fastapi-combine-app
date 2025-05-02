from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/combine", response_class=PlainTextResponse)
async def combine_text_and_file(
    input_string: str = Form(...),
    input_file: UploadFile = File(...)
):
    file_content = await input_file.read()
    file_text = file_content.decode('utf-8')
    
    combined_text = input_string + "Its deployed with azure,input text will be combined with File content" + "\n" + file_text
    return combined_text

# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.responses import PlainTextResponse
# from typing import Optional

# from .rag_pipeline import (
#     load_and_split_documents,
#     create_vectorstore,
#     create_retriever,
#     generate_rag_response
# )

# app = FastAPI()

# @app.post("/rag", response_class=PlainTextResponse)
# async def rag_api(
#     query: str = Form(...),
#     file: UploadFile = File(...)
# ):
#     try:
#         # Step 1: Read uploaded file bytes
#         file_bytes = await file.read()

#         # Step 2: Load and split documents
#         documents = load_and_split_documents(file_bytes=file_bytes)

#         # Step 3: Create vectorstore
#         vectorstore = create_vectorstore(documents)

#         # Step 4: Create retriever
#         retriever = create_retriever(vectorstore)

#         # Step 5: Generate response from RAG
#         response = generate_rag_response(query=query, retriever=retriever)

#         # Step 6: Return plain text response
#         return response

#     except Exception as e:
#         return PlainTextResponse(content=f"Error: {str(e)}", status_code=500)

