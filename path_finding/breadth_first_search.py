from .queue import Queue

def check_if_tile_is_passable(start_tile, next_tile):
    if next_tile is None:
        return False
    organizm = next_tile.get_organizm()
    if organizm is None:
        return True
    elif organizm.get_sila() <= start_tile.get_organizm().get_sila():
        return True
    else:
        return False


def breadth_first_search(start_tile, typ_goal_organism):

    queue = Queue()
    queue.put(start_tile)
    poprzednie = {}
    poprzednie[start_tile] = None
    goal_tile = None

    while not queue.empty():
        current = queue.get()
        if current is None:
            continue
        elif isinstance(current.get_organizm(), typ_goal_organism):
            goal_tile = current
            break

        for next_tile in current.get_sasiedzi():
            if not check_if_tile_is_passable(start_tile, next_tile):
                continue
            if next_tile not in poprzednie:
                queue.put(next_tile)
                poprzednie[next_tile] = current

    if goal_tile is None:
        return []

    path = []
    current = goal_tile
    while current != start_tile:
        path.append(current)
        current = poprzednie[current]
    path.reverse()
    return path
