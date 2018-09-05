-- +goose Up
-- SQL in this section is executed when the migration is applied.
CREATE TABLE usuario(
  id text primary key,
  rut text not null,
  dv text not null,
  nombre text not null,
  apellido_paterno text not null,
  apellido_materno text not null,
  fecha_nacimiento text not null,
  password text not null,
  sexo text,
  estado_civil text,
  hijos text,
  telefono text,
  email text,
  direccion text,
  comuna text,
  educacion text,
  renta text,
  sueldo_liquido integer,
  enfermedad_cronica text,
  creada_en datetime default current_timestamp
);

-- +goose Down
-- SQL in this section is executed when the migration is rolled back.
DROP TABLE usuario;