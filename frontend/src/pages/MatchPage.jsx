import React, { use, useEffect, useState } from "react";
import MatchHeader from "../components/MatchHeader";
import ExpandableBlock from "../components/CoefficientBlock";
import { useParams } from "react-router-dom";
import eventService from "../services/eventService";
import matchService from "../services/matchService";
import MatchSideBar from "../components/MatchSideBar";


const MatchPage = () => {
    const { id } = useParams();
    const [events, setEvents] = useState([]);
    const [match, setMatch] = useState({});
    const [bet, setBet] = useState({});
    const [betIsActive, setBetIsActive] = useState(false);
    const [activeEvent, setActiveEvent] = useState({});

    useEffect(() => {
        async function fetchData() {
            const eventsData = await eventService.getEvents({match_id: id});
            setEvents(eventsData);

            const matchData = await matchService.getMatch(id);
            setMatch(matchData);
        }
        fetchData();
    }, [])

    function onEventClick(betData, eventData) {
        setBetIsActive(true);
        setBet(betData);
        setActiveEvent(eventData);
    }

    return (
        <div className="bg-oneWinBlue-600 text-white font-inter p-6 flex-1">
            <div className="container grid grid-cols-6 gap-6">
                <div className="col-span-4">
                    <MatchHeader matchData={match} />
                    <div className="flex flex-col mt-4 gap-y-2">
                    {events.map((value) => (
                        <ExpandableBlock key={value.id} eventData={value} onEventClick={onEventClick}/>
                    ))}
                    </div>
                </div>

                <div className="col-span-2">
                    <MatchSideBar bet={bet} betIsActive={betIsActive} match={match} event={activeEvent}/>
                </div>
            </div>
        </div>
    );
};

export default MatchPage;
