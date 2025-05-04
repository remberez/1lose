import { NavLink } from "react-router-dom";

const MatchHeader = ({ matchData }) => {
    return (
        <div className="rounded-lg bg-pink-900">
            <div className="text-gray-300 text-xs px-5 py-4">
                Главная / Киберспорт / Dota 2 / {matchData.tournament.name}
            </div>
            <div className="flex items-center justify-center gap-x-4 mb-10">
                <div className="font-bold flex items-center gap-x-2">
                    <div>
                        {matchData.first_team.name}
                    </div>
                    <img
                        src={"http://localhost:8000/" + matchData.first_team.icon_path}
                        width={50}
                        height={50}
                    />
                </div>
                <div className="flex flex-col items-center text-xs">
                    <div>
                        Сегодня
                    </div>
                    <div>
                        18:00
                    </div>
                </div>
                <div className="font-bold flex items-center gap-x-2">
                    <img
                        src={"http://localhost:8000/" + matchData.second_team.icon_path}
                        width={50}
                        height={50}
                    />
                    <div>
                        {matchData.second_team.name}
                    </div>
                </div>
            </div>
            <div className="bg-rose-950 px-5 flex justiy-start gap-x-4 items-center py-1">
                <div>
                    X
                </div>
                <div className="flex gap-x-4 text-xs items-center">
                    <NavLink>
                        Матч
                    </NavLink>
                    <NavLink>
                        1 карта
                    </NavLink>
                    <NavLink>
                        2 карта
                    </NavLink>
                    <NavLink>
                        3 карта
                    </NavLink>
                </div>
            </div>
        </div>
    )
}

export default MatchHeader;