-- v002: Add namespace, resource_name, resource_kind to incidents
-- Applied: pending

ALTER TABLE incidents ADD COLUMN IF NOT EXISTS namespace VARCHAR;
ALTER TABLE incidents ADD COLUMN IF NOT EXISTS resource_name VARCHAR;
ALTER TABLE incidents ADD COLUMN IF NOT EXISTS resource_kind VARCHAR;

INSERT INTO schema_version (version, description) VALUES (2, 'Add namespace + resource columns to incidents');
