drop user prueba CASCADE;

create user prueba IDENTIFIED by duoc
QUOTA UNLIMITED on users;
GRANT CREATE SESSION, RESOURCE to prueba;