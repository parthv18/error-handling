// file: leak_event_listeners.js
const EventEmitter = require('events');
const emitter = new EventEmitter();

function attachListener(i) {
  const large = Buffer.alloc(200000); // ~200KB
  const listener = () => {
    // capture large in closure so it cannot be freed
    // do nothing
  };
  emitter.on('tick', listener);
}

// keep attaching listeners but never remove them
let i = 0;
setInterval(() => {
  attachListener(i++);
  emitter.emit('tick');
  const mem = process.memoryUsage();
  console.log(heapUsed=${Math.round(mem.heapUsed/1024/1024)}MB listeners=${emitter.listenerCount('tick')});
}, 300);
