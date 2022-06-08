drop user prueba2 CASCADE;

create user prueba2 IDENTIFIED by duoc
QUOTA UNLIMITED on users;
GRANT CREATE SESSION, RESOURCE to prueba2;