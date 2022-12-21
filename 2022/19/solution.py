import re, math


def read_input(name='input.txt'):
  with open(name, 'r') as f:
    for line in f:
      yield line.rstrip()


def add_lists(l1, l2):
  return [x+y for x,y in zip(l1, l2)]


class blueprint:
  def __init__(self, b):
    self.number = b[0]
    self.ore = [-b[1], 0, 0, 0]
    self.clay = [-b[2], 0, 0, 0]
    self.obsidian = [-b[3], -b[4], 0, 0]  # ore, clay
    self.geode = [-b[5], 0, -b[6], 0]  # ore, obsidian

  def search(self, time, cache, cur_max=0, resources=[0, 0, 0, 0], robots=[1, 0, 0, 0]):

    k = (time, *resources, *robots)
    if k in cache:
      return cache[k]

    v = resources[3] + robots[3] * time

    if v + time*(time-1) // 2 < cur_max:
      return cur_max

    if time == 0:
      return resources[3]  # geodes

    new_resources = add_lists(resources, robots)

    # geode robot check
    can_build_geode_robot = all(map(lambda x: x >= 0, add_lists(resources, self.geode)))
    new_robots_geode = add_lists(robots, [0, 0, 0, 1])
    new_resources_geode = add_lists(new_resources, self.geode)

    # obsidian robot check
    can_build_obsidian_robot = all(map(lambda x: x >= 0, add_lists(resources, self.obsidian)))
    new_robots_obsidian = add_lists(robots, [0, 0, 1, 0])
    new_resources_obsidian = add_lists(new_resources, self.obsidian)

    # clay robot check
    can_build_clay_robot = all(map(lambda x: x >= 0, add_lists(resources, self.clay)))
    new_robots_clay = add_lists(robots, [0, 1, 0, 0])
    new_resources_clay = add_lists(new_resources, self.clay)

    # ore robot check
    can_build_ore_robot = all(map(lambda x: x >= 0, add_lists(resources, self.ore)))
    new_robots_ore = add_lists(robots, [1, 0, 0, 0])
    new_resources_ore = add_lists(new_resources, self.ore)

    v = max(cur_max, v)
    v = max(self.search(time - 1, cache, v, new_resources, robots), v)

    if can_build_geode_robot:
      v = max(self.search(time - 1, cache, v, new_resources_geode, new_robots_geode), v)

    else:

      if can_build_obsidian_robot and robots[2] < -self.geode[2]:
        v = max(self.search(time - 1, cache, v, new_resources_obsidian, new_robots_obsidian), v)

      else:
        if can_build_clay_robot and robots[1] < -self.obsidian[1]:
          v = max(self.search(time - 1, cache, v, new_resources_clay, new_robots_clay), v)

        if can_build_ore_robot and \
          robots[0] <= -min(self.ore[0], self.clay[0], self.obsidian[0], self.geode[0]):
          v = max(self.search(time - 1, cache, v, new_resources_ore, new_robots_ore), v)

    cache[k] = v
    return v


blueprints = []
for l in read_input():
  b = list(map(int, re.findall(r'\d+', l)))
  blueprints.append(blueprint(b))


def p1():
  max_geodes = [x.search(24, {}) for x in blueprints]
  values = [x * y.number for x, y in zip(max_geodes, blueprints)]
  print(sum(values))


def p2():
  max_geodes = [x.search(32, {}) for x in blueprints[0:3]]
  print(math.prod(max_geodes))


p1()
p2()
