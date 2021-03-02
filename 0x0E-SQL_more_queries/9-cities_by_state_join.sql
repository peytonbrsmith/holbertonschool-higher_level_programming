-- SELECTS ALL CITIES
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE states.id = state_id
GROUP BY id;