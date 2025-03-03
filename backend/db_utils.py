import sqlite3
from datetime import datetime

DB_Name = "RAG-app.db"

def get_db_connection():
    conn = sqlite3.connect(DB_Name)
    conn.row_factory = sqlite3.Row
    return conn


def create_application_logs():
    conn = get_db_connection()
    conn.execute(
        '''create table if not exists application_logs
        (id integer primary key autoincrement, session_id text, user_query text, groq_response text, model text, created_at timestamp default current_timestamp)  
    ''')
    conn.close()

def create_document_store():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS document_store
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     filename TEXT,
                     upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.close()


def insert_application_logs(session_id, user_query, groq_response, model):
    conn = get_db_connection()
    conn.execute(
        'insert into application_logs(session_id, user_query, groq_response, model) values(?, ?, ?, ?)',
        (session_id, user_query, groq_response, model)
    )
    conn.commit()
    conn.close()

def get_chat_history(session_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
    'SELECT user_query, groq_response FROM application_logs WHERE session_id = ? ORDER BY created_at ASC', (session_id,))

    messages = []
    for row in cursor.fetchall():
        messages.extend([
            {'role': "human", "content": row['user_query'] },
            {'role': 'assistant', 'content': row['groq_response']}
        ])

    conn.close()
    return messages

def  insert_document_record(filename):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO document_store (filename) VALUES (?)', (filename,))
    file_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return file_id

def delete_document_record(file_id):
    conn = get_db_connection()
    conn.execute(
        'delete from document_store where id = ?', (file_id,)
    )
    conn.commit()
    conn.close()
    return True

def get_all_documents():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id, filename, upload_timestamp FROM document_store ORDER BY upload_timestamp DESC'
    )
    documents = cursor.fetchall()
    conn.close()
    return [
        {
            "id": str(doc["id"]),
            "filename": doc["filename"],
            "upload_timestamp": doc["upload_timestamp"]
        }
        for doc in documents
    ]


create_application_logs()
create_document_store()
