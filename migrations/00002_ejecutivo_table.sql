-- +goose Up
-- SQL in this section is executed when the migration is applied.
CREATE TABLE ejecutivo(
  id text primary key,
  rut text not null,
  dv text not null,
  nombre text not null,
  apellido_paterno text not null,
  apellido_materno text not null,
  fecha_nacimiento text not null,
  creada_en datetime default current_timestamp
);

-- +goose Down
-- SQL in this section is executed when the migration is rolled back.
DROP TABLE ejecutivo;