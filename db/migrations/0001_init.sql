-- Initial schema for chat sessions and messages
CREATE TABLE IF NOT EXISTS chatsession (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(200),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chatmessage (
    id VARCHAR(36) PRIMARY KEY,
    session_id VARCHAR(36) NOT NULL REFERENCES chatsession(id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_chatmessage_session_id ON chatmessage(session_id);
CREATE INDEX IF NOT EXISTS ix_chatmessage_created_at ON chatmessage(created_at);

