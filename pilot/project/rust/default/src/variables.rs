#![macro_use]
extern crate pilot_macro;
extern crate pilot_types;

use pilot_macro::*;

#[allow(unused_imports)]
use pilot_types::var::*;

#[derive(ConstNew, PilotAccess, PilotBindings)]
pub struct PlcVars {
  //insert your plc variables here
}


