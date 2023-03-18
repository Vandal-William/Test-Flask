BEGIN;

INSERT INTO "ticket" ("eventName","price", "discount", "status")
VALUES ('BLUE-ROSE', 12.99, 50, 'En boutique'),
('FEST-2023', 50.99, 0, 'En boutique'),
('BLACK-ALPHA', 22.99, 20, 'En boutique');

INSERT INTO "event" ("name", "style", "adress", "date", "eventType", "specificities")
VALUES ('BLUE-ROSE', 'POP', '11 rue novo 75008 paris', '11/03/2023', 'Concert', 'plain aire'),
('FEST-2023', 'Rap', '11 rue novo 75008 paris', '15/03/2023', 'Concert', 'plain aire'),
('BLACK-ALPHA', 'JAZZ', '12 rue momo 75009 paris', '25/03/2023', 'Concert', 'en salle');

INSERT INTO "musicians" ("groupName","description")
VALUES ('FESTA', 'Juste un groupe de plus'),
('MARIA', 'Juste un autre groupe de plus'),
('SUNDAY', 'et encore un groupe de plus');

COMMIT;