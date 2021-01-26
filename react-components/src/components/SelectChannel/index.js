import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom'

// Redux
import { connect, Provider } from 'react-redux';
import { bindActionCreators } from 'redux';
import { configureStore } from '../../store';
import { PersistGate } from 'redux-persist/integration/react'

// Components
import SelectChannelDropdown from './SelectChannelDropdown';

// Actions
import {
  setSyncModalOpenAction,
  setActiveChannelAction,
  setChannelsDbStaleAction,
} from '../../actions/index';

// api
import { 
  setChannelRequest,
} from '../../api/api';

const { store, persistor } = configureStore.getInstance();

// Component connected to Redux store
function Container(props) {
  const [dropdownChannels, setDropdownChannels] = useState(props.channels);
  const { isDbStale, storeChannels, channels } = props;

  useEffect(() => {
    /* If we have anything in the persisted Redux store
    at this point and db channels are stale we can assume that we should use that 
    instead of the data passed from db. If not we will use db. */
    const dbChannels = channels;
    if (storeChannels && isDbStale){
      setDropdownChannels(storeChannels);
      // Reset stale state now we are using the most up to date.
      props.setChannelsDbStale(false);
    } else {
      setDropdownChannels(dbChannels)
    }
      
  }, [storeChannels])

  const handleSelectChannel = async (e) => { 
    if (e.target.value){
      // update the active channel in the store and on the server
      props.setActiveChannel(e.target.value);
      await setChannelRequest(e.target.value);
      window.SELECTED_CHANNEL_ID = e.target.value;
    }
  };
  
  return (
    <SelectChannelDropdown channels={dropdownChannels} activeID={props.activeChannelID} onSelectChannel={(e) => handleSelectChannel(e)} />
  );
};

const mapDispatchToProps = (dispatch) => {
  return {
    dispatch,
    ...bindActionCreators({
      setSyncModalOpen: setSyncModalOpenAction,
      setActiveChannel: setActiveChannelAction,
      setChannelsDbStale: setChannelsDbStaleAction,
    }, dispatch),
  };
};

const mapStateToProps = state => ({
  storeChannels: state.channels.channels,
  activeChannelID: state.channels.activeChannelID,
  isDbStale: state.channels.isDbStale,
});

const ConnectedContainer = connect(mapStateToProps, mapDispatchToProps)(Container);

/* Entry point for DOM element render and subsequent button render.
This only deal with the above and handling API requests. The SyncChannel
component will manage logic.
*/
export const SelectChannelContainer = ({
  element,
  ...params
}) => {
  return (
    ReactDOM.render(
        <PersistGate loading={null} persistor={persistor}>
          <Provider store={store}>
            <ConnectedContainer {...params} />
          </Provider>
        </PersistGate>
      ,
      element || document.createElement('div') // for testing purposes
    )
  );
};

