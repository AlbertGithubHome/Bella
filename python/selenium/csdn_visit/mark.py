def arrangeWords(self, text: str) -> str:
        dt = collections.defaultdict(list)
        for w in text.split(' '):
            dt[len(w)].append(w)
        res = []
        for k in sorted(dt):
            res += [w.lower() for w in dt[k]]
        res = ' '.join(res)
        return res[0].upper() + res[1:]