-- +goose Up
-- SQL in this section is executed when the migration is applied.
CREATE TABLE credito(
  id integer primary key,
  fk_usuario_id integer not null,
  fk_estado_solicitud_id integer not null,
  monto integer default null,
  FOREIGN KEY (fk_usuario_id) REFERENCES usuario(id) ON DELETE CASCADE ON UPDATE NO ACTION,
  FOREIGN KEY (fk_estado_solicitud_id) REFERENCES estado_solicitud(id) ON DELETE CASCADE ON UPDATE NO ACTION
);

-- +goose Down
-- SQL in this section is executed when the migration is rolled back.
DROP TABLE credito;