-- Adminer 4.6.3-dev PostgreSQL dump

\connect "d2b87eob08vs03";

DROP TABLE IF EXISTS "alembic_version";
CREATE TABLE "public"."alembic_version" (
    "version_num" character varying(32) NOT NULL,
    CONSTRAINT "alembic_version_pkc" PRIMARY KEY ("version_num")
) WITH (oids = false);


DROP TABLE IF EXISTS "check_in";
DROP SEQUENCE IF EXISTS check_in_id_seq;
CREATE SEQUENCE check_in_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."check_in" (
    "id" integer DEFAULT nextval('check_in_id_seq') NOT NULL,
    "created" timestamp,
    "body" character varying(120),
    "user_id" integer,
    "location_id" integer,
    CONSTRAINT "check_in_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "check_in_location_id_fkey" FOREIGN KEY (location_id) REFERENCES location(id) NOT DEFERRABLE,
    CONSTRAINT "check_in_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "location";
DROP SEQUENCE IF EXISTS location_id_seq;
CREATE SEQUENCE location_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."location" (
    "id" integer DEFAULT nextval('location_id_seq') NOT NULL,
    "zipcode" character varying(32),
    "city" character varying(64),
    "state" character varying(16),
    "latitude" double precision,
    "longitude" double precision,
    "population" integer,
    CONSTRAINT "ix_location_zipcode" UNIQUE ("zipcode"),
    CONSTRAINT "location_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_location_city" ON "public"."location" USING btree ("city");

CREATE INDEX "ix_location_state" ON "public"."location" USING btree ("state");


DROP TABLE IF EXISTS "user";
DROP SEQUENCE IF EXISTS user_id_seq;
CREATE SEQUENCE user_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."user" (
    "id" integer DEFAULT nextval('user_id_seq') NOT NULL,
    "username" character varying(64),
    "email" character varying(120),
    "password_hash" character varying(128),
    CONSTRAINT "ix_user_email" UNIQUE ("email"),
    CONSTRAINT "ix_user_username" UNIQUE ("username"),
    CONSTRAINT "user_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


-- 2018-07-12 21:54:16.317848+00
