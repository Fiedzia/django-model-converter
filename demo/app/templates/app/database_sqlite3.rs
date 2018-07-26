use diesel::Connection;
use diesel::sqlite::SqliteConnection;


pub fn get_database_url() -> String {
    "{{ app_database.settings.NAME }}".to_string()
}


pub fn establish_connection() -> SqliteConnection {

    let database_url = get_database_url();
    SqliteConnection::establish(&database_url).expect(&format!("Error connecting to {}", database_url))

}
