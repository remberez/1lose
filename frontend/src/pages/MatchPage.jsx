import React, { useEffect, useState } from "react";
import MatchHeader from "../components/MatchHeader";
import ExpandableBlock from "../components/CoefficientBlock";
import { useParams } from "react-router-dom";
import eventService from "../services/eventService";

const matchData = {
  second_team_id: 13,
  updated_at: "2025-05-03T06:17:53.649031",
  score: [0, 0],
  id: 14,
  best_of: 1,
  date_start: "2025-05-06T02:11:32.851000+00:00",
  date_end: null,
  game_id: null,
  first_team_id: 12,
  win_event_id: 22,
  tournament_id: 9,
  created_at: "2025-05-03T06:12:09.229134",
  win_event: {
    match_id: 14,
    first_outcome_id: 43,
    id: 22,
    updated_at: "2025-05-03T06:17:25.694050",
    map_id: null,
    name: "Победа",
    second_outcome_id: 44,
    created_at: "2025-05-03T06:17:25.694047",
    updated_by: 5,
    second_outcome: {
      coefficient: 1.5,
      id: 44,
      name: "Победа Team Spirit",
    },
    first_outcome: {
      coefficient: 2.5,
      id: 43,
      name: "Победа Virtus Pro",
    },
  },
  first_team: {
    game_id: 44,
    icon_path: "media/teams/85123f7e-726a-4b42-9b64-147627753e18.png",
    name: "Team Spirit",
    id: 12,
    game: {
      description: "The Dota 2",
      icon_path: "media/games/fa59017a-6b72-44a2-83f8-f8625f0273c6.png",
      name: "Dota 2",
      id: 44,
    },
  },
  second_team: {
    game_id: 44,
    icon_path: "media/teams/592b6a74-4ba1-4af3-8808-fdfb5bfaac12.png",
    name: "Virtus Pro",
    id: 13,
    game: {
      description: "The Dota 2",
      icon_path: "media/games/fa59017a-6b72-44a2-83f8-f8625f0273c6.png",
      name: "Dota 2",
      id: 44,
    },
  },
  tournament: {
    game_id: 44,
    description: "the dota 2 tournament",
    created_at: "2025-04-17T11:57:48.963140",
    name: "The International 15",
    id: 9,
    updated_at: "2025-04-17T11:57:48.963147",
    game: {
      description: "The Dota 2",
      icon_path: "media/games/fa59017a-6b72-44a2-83f8-f8625f0273c6.png",
      name: "Dota 2",
      id: 44,
    },
  },
};


const MatchPage = () => {
    const { id } = useParams();
    const [events, setEvents] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const eventsData = await eventService.getEvents({match_id: id});
            console.log(eventsData)
            setEvents(eventsData);
        }
        fetchData();
    }, [])

    return (
        <div className="bg-oneWinBlue-600 text-white font-inter p-6 flex-1">
            <div className="max-w-7xl mx-auto">
                <MatchHeader matchData={matchData}/>
                <div className="flex flex-col mt-4 gap-y-2">
                    {
                        events.map(value => (
                            <ExpandableBlock eventData={value}/>
                        ))
                    }
                </div>
            </div>
        </div>
    );
};

export default MatchPage;
