def divination(C):
    match C.rank:
        case cards.RankEnum.SIX:
            return 'Влюблений: Любов, стосунки, вибір.'
        case cards.RankEnum.SEVEN:
            return 'Колесо Фортуни: Рух, зміна, циклічність.'
        case cards.RankEnum.EIGHT:
            return 'Сила: Самоконтроль, воля, мужність.'
        case cards.RankEnum.NINE:
            return 'Осьминіг: Таємниці, інтуїція, розуміння.'
        case cards.RankEnum.TEN:
            return 'Колода: Успіх, досягнення, визнання.'
        case cards.RankEnum.JACK:
            return 'Високий жрець: Державність, релігія, традиції.'
        case cards.RankEnum.QUEEN:
            return 'Вівця: Послух, покірність, безпека.'
        case cards.RankEnum.KING:
            return 'Смерть: Зміна, перехід, перетворення.'
        case cards.RankEnum.ACE:
            return 'Шалений: Необдуманість, ризик, безлад.'


def getcards(D, N):
    l = list()
    for i in range(1, N+1):
        c = D.get_top()
        l.append(c)
    return l

def main(args):
    d = cards.Deck()
    d.shuffle()
    if len(args) <= 1:
        print("error: set number")
        return
    if int(args[1]) <= 0 or int(args[1]) > len(d):
        print(f'error: 1 <= card <={len(d)}')
        return

    c = getcards(d, int(args[1]));
    for l in c:
        print(f'{l} = {divination(l)}')
    return

if __name__ == '__main__':
    import sys
    import random
    import argparse
    import cards
    sys.exit(main(sys.argv))
