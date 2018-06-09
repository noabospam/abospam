from Mailman import mm_cfg
import sys

def update_banlist(list, filename_banlist):
  print list.real_name+":"
  save = False
  abospam = open( filename_banlist ).read().splitlines()
  delete = [pattern for pattern in list.ban_list if pattern.endswith('(ABOSPAM)?') and pattern not in abospam ]
  print "  delete:"
  if delete:
    for pattern in delete:
      print "    "+pattern
      list.ban_list.remove(pattern)
    save = True
  new = [ pattern for pattern in abospam if not pattern in list.ban_list ]
  print "  append:"
  if new:
    for pattern in new:
      print "    "+pattern
      list.ban_list.append(pattern)
    save = True
  if save:
    list.Save()
