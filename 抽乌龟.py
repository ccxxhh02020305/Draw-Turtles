import random


def create_card():   # 创建牌堆
    deck = ['A','A','A','A',
            '2','2','2','2',
            '3','3','3','3',
            '4','4','4','4',
            '5','5','5','5',
            '6','6','6','6',
            '7','7','7','7',
            '8','8','8','8',
            '9','9','9','9',
            '10','10','10','10',
            'J','J','J','J',
            'Q','Q','Q','Q',
            'K','K','K','K',]
    deck.extend(['大王', '小王'])
    return deck


def deal_cards(removed_card,num):   # 发牌
    per_card = 53 // num
    spare_card = 53 % num
    players = [[] for _ in range(num)]
    random.shuffle(removed_card)
    for i in range(0,num):
        players[i] = removed_card[per_card*i:per_card*(i+1)]
    players[num-1] = players[num-1] + [removed_card[spare_card]]
    return players

def clean(players,num):   # 消对子
    for i in range(0,num):
        used_card = []
        for a in players[i]:
            if a not in used_card:
                used_card.append(a)
                players[i].remove(a)

        min_joker_count = 0
        max_joker_count = 0
        for item in used_card:
            if item == '小王':
                min_joker_count += 1
            if item == '大王':
                max_joker_count += 1

        if min_joker_count == 1 and max_joker_count == 1:
            used_card.remove('小王')
            used_card.remove('大王')

        for aa in players[i]:
            for item in used_card:
                if item == aa:
                    players[i].remove(aa)
                    used_card.remove(item)
                    continue

        players[i] = used_card

    return players

def draw(old_players,num):   # 从下一玩家手里抽牌
    players = old_players
    for i in range(0, num):
        if not players[i]:
            print(f"玩家{i + 1}获胜")
            return False
    for i in range(0,num-1):
        drawn_card = random.choice(players[i+1])
        players[i].append(drawn_card)
        players[i+1].remove(drawn_card)
    drawn_card1 = random.choice(players[0])
    players[num-1].append(drawn_card1)
    players[0].remove(drawn_card1)

    return players




def main():
    card = create_card()
    while True:
        num = int(input("请输入玩家数量（建议人数3-6人）："))
        if 3 <= num <= 6:
            break
        elif num < 3:
            print("请输入大于2的数字！")
        else:
            print("请输入小于7的数字！")

    drawn_card = random.choice(card)
    card.remove(drawn_card)
    print(f"一号位玩家，本局抽出的牌是：{drawn_card}")

    dealed_card = deal_cards(removed_card = card,num=num)
    for i in range(0,num):
        print(f"{i+1}号位玩家，您的手牌为：{dealed_card[i]}")

    cleaned_card = clean(players=dealed_card,num=num)
    player1 = cleaned_card[0]
    print(f"一号位玩家，您的手牌为：{player1}")

    new_card = draw(old_players=cleaned_card,num=num)
    round = 0
    # 循环开始
    while True:
        cleaned_card = clean(players=new_card,num=num)
        for i in range(0,num):
            if not cleaned_card[i]:
                print(f"玩家{i+1}获胜")
                return False
                break
        new_card = draw(old_players=cleaned_card,num=num)
        player1 = new_card[0]
        round += 1

        # 结束判断
        total_cards = sum(len(p) for p in new_card)
        if total_cards == 1:
            for i, card_name in enumerate(players):
                if card_name:
                    print(f"乌龟牌在玩家{i + 1}手中，是{card_name}")
                    return False


        for i in range(0,num):
            if len(new_card[i]) == 0:
                print(f"{i+1}号位玩家赢了")
                return False

        if round > 20000:
            print(f"已经过{round}轮循环，此情形无解")
            for i in range(0,num):
                print(new_card[i])
            return False


if __name__ == "__main__":
    main()