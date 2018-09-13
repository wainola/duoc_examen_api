-- +goose Up
-- SQL in section 'Up' is executed when this migration is applied
ALTER TABLE usuario ADD COLUMN role text;

-- +goose Down
-- SQL section 'Down' is executed when this migration is rolled back
BEGIN TRANSACTION;
ALTER TABLE usuario RENAME TO usuario_temp;

CREATE TABLE usuario(
  id text primary key,
  rut text not null,
  dv text not null,
  nombre text not null,
  apellido_paterno text not null,
  apellido_materno text not null,
  fecha_nacimiento text not null,
  password text,
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
  creada_en datetime default current_timestamp,
  role text
);

INSERT INTO usuario
SELECT id, rut, dv, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, password, sexo, estado_civil, hijos, telefono, email, direccion, comuna, educacion, renta, sueldo_liquido, enfermedad_cronica, creada_en, 'usuario'
FROM usuario_tmp;

DROP TABLE usuario_temp;

COMMIT;