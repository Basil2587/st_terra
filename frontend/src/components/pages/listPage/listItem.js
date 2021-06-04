import React, {useEffect, useState} from 'react';
// import AppHeader from '../../appHeader/appHeader';
import plus from '../../../img/plus.svg';

const ListItem = ({toggleList,  data = [], img}) => {

    const [checked, setChecked] = useState(0);
    const handleInputChange = (event) => {
        const target = event.target;

        // data = [...data.slice(0, target.id), ...data.slice(target.id + 1)];

        // console.log(target.id)
        // const index = data.findIndex((point) => point.id === target.id);
        // setChecked([...data.slice(0, index), ...data.slice(index + 1)]);
        // console.log(data)

        // setLine((checked * 26) / data.length)

        target.checked ? setChecked(checked + 1) : setChecked(checked - 1); 
    }

    // const t = (checked * 100) / data.length;
    const [line, setLine] = useState(0)

    return (
        <div className='wrraper'>
            <div className="d-flex flex-column scroll bg-white">
                <div className="overflow">
                    <div class="name_plus">
                        <span class="name-title" href="">{data.title}</span>
                        <div onClick={toggleList}><img className='add' src={plus} alt="add"/></div>
                    </div>
                    <div class="rating">
                        <p class="number">{checked}/{data.length}</p>
                        {/* <div className="line"></div>
                        <div style={{width: `${line}%`}} className="linee"></div> */}
                    </div> 
                        {
                            data.map((item, index) => {
                            return (
                                    <label className="checkbox d-flex" id={index}>
                                        <input onChange={handleInputChange} id={index} type="checkbox" />
                                        <p>{item.data}</p>
                                    </label>
                                )
                            })
                        }

                </div>
                <div class="exit-btn btn1">
                    <button class="btnn" type="btn" name="exit">Показать завершенные</button>
                </div>

            </div>
            <div className="wrapper__img-list bg-white">
                {
                    img ? <img className="img-list" src={img}/> : null
                }
            </div>
        </div>            
    );
}





export default ListItem; 