a = input().strip()
if '::' in a:
    l, r  = a.split('::', 1)
    l = l.split(':') if l else []
    r = r.split(':') if r else []
else:
    l = a.split(':')
    r = []
l = [part.zfill(4) for part in l]
r = [part.zfill(4) for part in r]
t = 8 - (len(l) + len(r))
ans = l + ['0000'] * t + r
print(':'.join(ans))

