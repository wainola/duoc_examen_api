-- +goose Up
-- SQL in this section is executed when the migration is applied.
CREATE TABLE estado_solicitud(
  id integer primary key,
  estado_solicitud text not null,
  creada_en datetime default current_timestamp
);

-- +goose Down
-- SQL in this section is executed when the migration is rolled back.
DROP TABLE estado_solicitud;