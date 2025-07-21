% Facts
parent(john, mary).    % John is Mary’s parent
parent(mary, susan).   % Mary is Susan’s parent
male(john).
female(mary).
female(susan).

% Rules
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
