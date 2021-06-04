import React from 'react';
import '../../index.css';
import {Link} from 'react-router-dom';
import imgArr from "../../img/arrow.svg";
import pict1 from "../../img/1.svg";
import pict2 from "../../img/2.svg";
import pict3 from "../../img/3.svg";
import pict4 from "../../img/4.svg";
import pict5 from "../../img/5.svg";
import pict6 from "../../img/6.svg";
import pict7 from "../../img/7.svg";
import pict8 from "../../img/8.svg";

export const Navbar = () => {
    return (
    <div className="left-menu">

        <div className="wrap-1">
            <h1 className="title">Samo</h1>
            
        </div>

        {/* <!--<img className="line" src="../img/line.svg">--> */}

        <div className="nav">
            <img className="nav-arrow" src={imgArr} alt="arrow"/>
            <Link href="" className="nav-text">Свернуть</Link>
        </div>

        <div className="list list-items">
                <div className="list-item">
                    <img className="pict" src={pict1}/>
                    <Link href="" className="spisok">Колесо баланса</Link>
                </div>
                <div className="list-item">
                    <img className="pict" src={pict2}/>
                    <Link href="" className="spisok">Дневник</Link>
                </div>
                <div className="list-item">
                    <img className="pict" src={pict3}/>
                    <Link href="" className="spisok">Календарь</Link>
                </div>
                <div className="list-item">
                    <img className="pict" src={pict4}/>
                    <Link href="" className="spisok">Мои цели</Link>
                </div>
                <div className="list-item">
                    <img className="pict" src={pict5}/>
                    <Link href="" className="spisok">Мои ценности</Link>
                </div>
                <div className="list-item">
                    <img className="pict" src={pict6}/>
                    <Link to="list" className="spisok">Списки</Link>
                </div>
                <div className="list-item">
                    <img className="pict" src={pict7}/>
                    <Link to="results" className="spisok">Итоги</Link>
                </div>
                
        </div>

        <div className="end">
            <div className="list-item">
                <img className="pict" src={pict8}/>
                <Link href="" className="set">Настройки</Link>
            </div>
            <div className="exit">
                <button className="btn-exit" type="btn" name="exit">Выйти</button>
            </div>
        </div>
    </div>
    )
}

export default Navbar;
