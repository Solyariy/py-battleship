from dataclasses import dataclass


@dataclass
class Deck:
    row: int
    column: int
    is_alive: bool = True


class Ship:
    def __init__(
            self,
            start: tuple[int, int],
            end: tuple[int, int],
            is_drowned: bool = False
    ) -> None:
        self.is_drowned = is_drowned
        self.decks: list[Deck] = [Deck(*start)]
        current = start
        while current != end:
            row, column = current
            row += row < end[0]
            column += column < end[1]
            current = row, column
            self.decks.append(Deck(row, column))

    def get_deck(self, row: int, column: int) -> Deck | None:
        for item in self.decks:
            if item.row == row and item.column == column:
                return item

    def fire(self, row: int, column: int) -> str:
        if deck := self.get_deck(row, column):
            deck.is_alive = False
            if not any(deck.is_alive for deck in self.decks):
                self.is_drowned = True
                return "Sunk!"
            return "Hit!"
        return "Miss!"


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        self.field = {}
        for row in ships:
            ship = Ship(*row)
            for deck in ship.decks:
                self.field[deck.row, deck.column] = ship

    def fire(self, location: tuple[int, int]) -> str:
        if ship := self.field.get(location):
            return ship.fire(*location)
        return "Miss!"
