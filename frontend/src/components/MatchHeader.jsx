import { NavLink } from "react-router-dom";


function MatchTime({ dateStart }) {
    const now = new Date();
    const matchDate = new Date(dateStart);
  
    const isSameDay =
      now.getFullYear() === matchDate.getFullYear() &&
      now.getMonth() === matchDate.getMonth() &&
      now.getDate() === matchDate.getDate();
  
    const hasStarted = now > matchDate;
  
    const formatTime = (date) => {
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    };
  
    const formatDate = (date) => {
      const day = date.getDate().toString().padStart(2, '0');
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      return `${day}.${month}`;
    };
  
    if (hasStarted && !isSameDay) {
      return (
        <div className="flex flex-col items-center text-xs text-red-600 font-semibold">
          Live
        </div>
      );
    }
  
    if (isSameDay) {
      return (
        <div className="flex flex-col items-center text-xs">
          <div>Сегодня</div>
          <div>{formatTime(matchDate)}</div>
        </div>
      );
    }
  
    // если матч не сегодня
    return (
      <div className="flex flex-col items-center text-xs">
        <div>Дата - {formatDate(matchDate)}</div>
        <div>Время - {formatTime(matchDate)}</div>
      </div>
    );
}
  

const MatchHeader = ({ matchData }) => {
    return (
        <div className="rounded-lg bg-blue-600">
            <div className="text-gray-300 text-xs px-5 py-4">
                Главная / Киберспорт / Dota 2 / {matchData.tournament?.name}
            </div>
            <div className="flex items-center justify-center gap-x-4 mb-10">
                <div className="font-bold flex items-center gap-x-2">
                    <div>
                        {matchData.first_team?.name}
                    </div>
                    <img
                        src={"http://localhost:8000/" + matchData.first_team?.icon_path}
                        width={50}
                        height={50}
                    />
                </div>
                <MatchTime dateStart={matchData.date_start} />

                <div className="font-bold flex items-center gap-x-2">
                    <img
                        src={"http://localhost:8000/" + matchData.second_team?.icon_path}
                        width={50}
                        height={50}
                    />
                    <div>
                        {matchData.second_team?.name}
                    </div>
                </div>
            </div>
            <div className="bg-blue-800 px-5 flex justiy-start gap-x-4 items-center py-1">
                <div>
                    X
                </div>
                <div className="flex gap-x-4 text-xs items-center">
                    <NavLink>
                        Матч
                    </NavLink>
                    {Array.from({ length: matchData.best_of }, (_, i) => (
                        <NavLink key={i}>
                            {i + 1} карта
                        </NavLink>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default MatchHeader;