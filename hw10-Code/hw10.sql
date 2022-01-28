.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE sizes.min < dogs.height AND sizes.max >= dogs.height;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child AS name FROM parents, dogs WHERE parent = dogs.name ORDER BY height DESC;


-- Sentences about siblings that are the same size
CREATE TABLE pairs AS
  SELECT a.child AS first, b.child AS second, c.size AS samesize FROM parents AS a, parents AS b, size_of_dogs AS c, size_of_dogs AS d
  WHERE a.parent = b.parent AND a.child < b.child AND a.child = c.name AND b.child = d.name AND c.size = d.size;
CREATE TABLE sentences AS
  SELECT "The two siblings, " || first || " plus " || second || " have the same size: " || samesize 
  FROM pairs;