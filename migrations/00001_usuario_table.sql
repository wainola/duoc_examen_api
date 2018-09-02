-- +goose Up
-- SQL in this section is executed when the migration is applied.
CREATE TABLE usuario(
  id integer primary key,
  rut text not null,
  dv text not null,
  nombre text not null,
  apellido_paterno text not null,
  apellido_materno text not null,
  fecha_nacimiento text not null,
  password text not null,
  sexo text not null,
  estado_civil text not null,
  hijos text not null,
  telefono text not null,
  email text not null,
  direccion text not null,
  comuna text not null,
  educacion text not null,
  renta text not null,
  sueldo_liquido integer not null,
  enfermedad_cronica text not null,
  creada_en datetime default current_timestamp
);

-- +goose Down
-- SQL in this section is executed when the migration is rolled back.
DROP TABLE usuario;