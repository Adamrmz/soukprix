-- Run this once in Supabase → SQL Editor to enable live cross-device cart sync.
-- Without it, the cart still works (save/load), it just won't push updates to
-- other open sessions/devices in real time.
alter publication supabase_realtime add table cart_items;
