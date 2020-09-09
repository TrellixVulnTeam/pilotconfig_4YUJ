/*
 THIS FILE IS AUTOGENERATED. DO NOT EDIT
*/

#[repr(C)]
pub struct plc_dev_t {
    pub m1: u8,
    pub m2: u8,
    pub m3: u8,
}

pub trait PilotBindings {
    const MAX_FIELD_NUM: u16;
    const VARIABLES: &'static [VariableInfo];

    fn set_from_pilot_bindings(&mut self, plc_mem: &plc_dev_t);
    fn write_to_pilot_bindings(&self, plc_mem: &mut plc_dev_t);
    fn plc_varnumber_to_variable(
        &mut self,
        number: u16,
    ) -> Option<&mut dyn pilot_types::var::MemVar>;
}

#[derive(Debug)]
#[repr(C)]
pub struct VariableInfo {
    pub name: &'static str,
    pub ty: &'static str,
    pub fields: &'static [VariableInfo], // for compound types
    pub field_number_offset: u16,        // field number adjustments for compound fields
    pub number: u16,                     // only valid when fields len is zero
}
