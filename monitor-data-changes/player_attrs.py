import pandas as pd


if __name__ == '__main__':
    players_15 = pd.read_csv("/in/players_15.csv")
    players_16 = pd.read_csv("/in/players_16.csv")
    players_17 = pd.read_csv("/in/players_17.csv")
    players_18 = pd.read_csv("/in/players_18.csv")
    players_19 = pd.read_csv("/in/players_19.csv")
    players_20 = pd.read_csv("/in/players_20.csv")

    players_attrs = pd.concat([
        players_15.assign(fifa=lambda x: 15),
        players_16.assign(fifa=lambda x: 16),
        players_17.assign(fifa=lambda x: 17),
        players_18.assign(fifa=lambda x: 18),
        players_19.assign(fifa=lambda x: 19),
        players_20.assign(fifa=lambda x: 20)
    ])
    players_attrs = players_attrs.loc[:, [
        "sofifa_id", "overall", "potential", "fifa", "pace", "shooting",
        "passing", "dribbling", "defending", "physic"
    ]]
    players_attrs = players_attrs.reset_index(drop=True)
    players_attrs.to_csv("/out/out.csv", index=False)

    with open('/out/pk', 'wt') as file:
        file.write('sofifa_id,fifa')
