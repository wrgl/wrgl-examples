import pandas as pd


if __name__ == '__main__':
    players_15 = pd.read_csv("/in/players_15.csv")
    players_16 = pd.read_csv("/in/players_16.csv")
    players_17 = pd.read_csv("/in/players_17.csv")
    players_18 = pd.read_csv("/in/players_18.csv")
    players_19 = pd.read_csv("/in/players_19.csv")
    players_20 = pd.read_csv("/in/players_20.csv")

    players = pd.concat([
        df.loc[:, ["sofifa_id", "short_name", "long_name", "dob"]]
        for df in [players_15, players_16, players_17, players_18, players_19, players_20]
    ])
    players = players.set_index("sofifa_id")
    players = players[~players.index.duplicated()]

    players.to_csv("/out/out.csv")

    with open('/out/pk', 'wt') as file:
        file.write('sofifa_id')
