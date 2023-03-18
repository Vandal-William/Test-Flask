BEGIN;

DROP TABLE IF EXISTS "ticket", "event", "musicalGroup", "musicians";

CREATE TABLE "ticket"(
    "id" INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "eventName" VARCHAR(255) NOT NULL,
    "price" DECIMAL NOT NULL,
    "discount" INTEGER,
    "status" VARCHAR(255) NOT NULL,
    "createdAt" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedAt" TIMESTAMPTZ
);

CREATE TABLE "event"(
    "id" INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "style" VARCHAR(255) NOT NULL,
    "adress" VARCHAR(255) NOT NULL,
    "date" DATE NOT NULL,
    "eventType" VARCHAR(255) NOT NULL,
    "specificities" VARCHAR(255) NOT NULL,
    "createdAt" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedAt" TIMESTAMPTZ    
);

CREATE TABLE "musicians"(
    "id" INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "groupName" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "createdAt" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedAt" TIMESTAMPTZ
);

COMMIT;