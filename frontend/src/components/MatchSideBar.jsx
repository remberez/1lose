import { useState } from "react";
import { BsTicketPerforated } from "react-icons/bs";
import { FaGamepad } from "react-icons/fa";
import { CgClose } from "react-icons/cg";
import betService from "../services/betService";
import { Link, useNavigate } from "react-router-dom";
import { userStore } from "../stores/authStore";

const MatchSideBar = ({ bet, betIsActive, match, event }) => {
    const [amount, setAmount] = useState(0);
    const navigate = useNavigate();
  
    const handleQuickAmount = (val) => {
      setAmount(prev => prev + val);
    };
  
    const possibleWin = (amount * (bet?.coefficient || 0)).toFixed(2);

    async function onButtonClick() {
        const responseData = await betService.createBet({event_id: event.id, outcome_id: bet.id, amount});
        
        if (responseData.status === 200) {
            navigate("/")
        }
    }
  
    return (
      <div className="bg-red-800 rounded-md p-2">
        <h2 className="text-white font-bold text-lg mb-2">Купон</h2>
  
        {betIsActive ? (
          <div className="bg-white my-4 rounded-md p-2 text-black text-sm">
            <div className="flex gap-x-2">
              <FaGamepad color="black" size={20} />
              <div>
                <div>{match.first_team?.name} - {match.second_team?.name}</div>
                <div className="text-sm font-bold">{event.name} - {bet.name}</div>
              </div>
              <div className="ml-auto font-semibold self-center border-2 p-2 border-gray-300 rounded-md">
                {bet.coefficient}
              </div>
              <button className="self-center">
                <CgClose />
              </button>
            </div>
  
            <div className="mt-3">
              <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(Number(e.target.value))}
                className="w-full p-2 border rounded-md mb-2"
                placeholder="Введите сумму ставки"
              />
  
              <div className="flex gap-2 mb-2 flex-wrap">
                {[50, 100, 500, 1000].map((val) => (
                  <button
                    key={val}
                    onClick={() => handleQuickAmount(val)}
                    className="px-3 py-1 bg-gray-200 rounded hover:bg-gray-300"
                  >
                    +{val}
                  </button>
                ))}
              </div>
  
              <div className="text-sm font-medium">
                Возможный выигрыш:{" "}
                <span className="font-bold">{possibleWin}</span>
              </div>
              {
                userStore.isAuth ?
                <button className="bg-blue-600 text-white block w-full mt-2 py-2 rounded-md" onClick={onButtonClick}>
                    Заключить пари на { amount }
                </button> :
                <Link className="bg-blue-600 text-white block w-full mt-2 py-2 rounded-md text-center" to="/login">
                    Авторизуйтесь, что бы сделать ставку
                </Link>
              }
            </div>
          </div>
        ) : (
          <div className="flex flex-col items-center my-7 text-white">
            <BsTicketPerforated size={35} />
            <div className="mt-2">Выберите исход события</div>
            <div className="text-sm text-gray-300">
              Чтобы заключить пари
            </div>
          </div>
        )}
      </div>
    );
};

export default MatchSideBar;