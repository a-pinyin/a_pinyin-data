use rusqlite as sqlite;

pub fn sqlite_version() -> &'static str {
    sqlite::version()
}

// TODO
